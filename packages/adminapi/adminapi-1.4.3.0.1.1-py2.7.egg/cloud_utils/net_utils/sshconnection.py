# Software License Agreement (BSD License)
#
# Copyright (c) 2009-2011, Eucalyptus Systems, Inc.
# All rights reserved.
#
# Redistribution and use of this software in source and binary forms, with or
# without modification, are permitted provided that the following conditions
# are met:
#
#   Redistributions of source code must retain the above
#   copyright notice, this list of conditions and the
#   following disclaimer.
#
#   Redistributions in binary form must reproduce the above
#   copyright notice, this list of conditions and the
#   following disclaimer in the documentation and/or other
#   materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Author: matt.clark@eucalyptus.com
"""
Created on Mar 7, 2012
@author: clarkmatthew

simple class to establish an ssh session
example usage:
    import sshconnection
    ssh = SshConnection( '192.168.1.1', keypath='/home/testuser/keyfile.pem')

    #use sys() to get either a list of output lines or a single string buffer depending
    on listformat flag
    output = ssh.sys('ls /dev/sd*',timeout=10)
    print output[0]
    print ssh.lastcmd+" exited with code: "+str(ssh.lastexitcode)

    #...or use cmd to get a dict of output, exitstatus, and elapsed time to execute...
    out = ssh.cmd('ping 192.168.1.2 -c 1 -W 5')

     print out['cmd']+" exited with status:"+out['status']+", elapsed time:"+out['elapsed']
     print out['output']

example with proxy:
    import sshconnection

    instance_private_ip = '10.1.1.5'
    instance_user = 'root'
    instance_keypath = '/tmp/instancekey.pem'

    proxy_ip = '192.168.1.2'
    proxy_username = 'testuser'
    #proxy_password = 'foo'
    proxy_keypath = '/home/testuser/keyfile.pem'


    example output from ipython:

    In[4]: instance_ssh = SshConnection( instance_private_ip, username=instance_user,
                                         keypath=instance_keypath,
            proxy=SshConnection(proxy_ip, proxy_username = proxy_username,
                                proxy_keypath = proxy_keypath, debug_connect = True)
    ssh_connect args:
    hostname:10.1.1.5
    username:root
    password:None
    keypath:/tmp/instancekey.pem
    timeout:60
    retry:1
    IPV6 DNS lookup disabled, do IPV4 resolution and pass IP to connect()
    10.1.1.5, is already an ip, dont do host lookup...
    192.168.1.2, is already an ip, dont do host lookup...
    SSH connection attempt(1 of 2), host:'root@10.1.1.5', using ipv4:10.1.1.5,
                                    thru proxy:'192.168.1.2'
    Using Keypath:/tmp/instancekey.pem
    SSH - Connected to 10.1.1.5 via proxy host:192.168.1.2:22

    In [5]: instance_ssh.sys('hostname')
    Out[5]: ['euca_10_1_1_5.eucalyptus_cloud.com']

"""

import copy
from httplib import HTTPConnection, CannotSendRequest
from cloud_utils.log_utils.eulogger import  Eulogger
import os
import paramiko
from paramiko.sftp_client import SFTPClient
import re
import select
import socket
import time
import types
import sys
from urlparse import urlparse
import termios
import tty


def get_ipv4_lookup(hostname, port=22, debug_method=None, verbose=False):
    """
    Do an ipv4 lookup of 'hostname' and return list of any resolved ip addresses

    :param hostname: hostname to resolve
    :param port: port to include in lookup, default is ssh port 22
    :param verbose: boolean to print addditional debug
    :return: list of ip addresses (strings in a.b.c.d format)
    """
    if not verbose or not debug_method:
        def debug_method(msg):
            return

    get_ipv4_ip = False
    iplist = []
    try:
        if socket.inet_aton(hostname):
            ipcheck = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
            if not ipcheck.match(hostname):
                get_ipv4_ip = True
        debug_method(str(hostname) + ", is already an ip, dont do host lookup...")
        # This is already an ip don't look it up (regex might be better here?)
    except socket.error:
        get_ipv4_ip = True
    if get_ipv4_ip:
        try:
            # ipv4 lookup host for ssh connection...
            addrs = socket.getaddrinfo(hostname, port, socket.AF_INET, socket.IPPROTO_IP,
                                       socket.IPPROTO_TCP)
            for addr in addrs:
                iplist.append(str(addr[4][0]))
            debug_method('Resolved hostname:' + str(hostname) + ' to IP(s):' +
                         ",".join(iplist), verbose=verbose)
        except Exception, de:
            debug_method('Error looking up DNS ip for hostname:' + str(hostname) +
                         ", err:" + str(de))
    else:
        # hostname is an ipv4 address...
        iplist = [hostname]
    return iplist


class SFTPifc(SFTPClient):

    def debug(self, msg, verbose=True):
        print (str(msg))

    def get(self, remotepath, localpath, callback=None):
        try:
            super(SFTPifc, self).get(remotepath, localpath, callback=callback)
        except Exception, ge:
            self.debug('Error during sftp get. Remote:"{0}", Local:"{1}"'
                       .format(remotepath, localpath))
            raise type(ge)('Error during sftp get. Remotepath:"{0}", Localpath:"{1}".\n Err:{2}'
                           .format(remotepath, localpath, str(ge)))

    def put(self, localpath, remotepath, callback=None, confirm=True):
        try:
            super(SFTPifc, self).put(localpath=localpath, remotepath=remotepath,
                                     callback=callback, confirm=confirm)
        except Exception, pe:
            raise type(pe)('Error during sftp put. Remotepath:"{0}", Localpath:"{1}".\n Err:{2}'
                           .format(remotepath, localpath, str(pe)))


class SshCbReturn():
    def __init__(self, stop=False, statuscode=-1, settimer=0, buf=None, sendstring=None,
                 nextargs=None, nextcb=None, removecb=False):
        """
        Used to return data from an ssh cmd callback method that can be used to handle
        output as it's rx'd instead of waiting for the cmd to finish and returned buffer.
        See SshConnection.cmd() for more info.
        The call back must return type SshCbReturn.
        :param stop: If cb returns stop==True, recv loop will end, and channel will be closed,
                     cmd will return.
        :param settimer: if cb settimer is > 0, timer timeout will be adjusted for this time
        :param statuscode: if cb statuscode is != -1 cmd status will return with this value
        :param nextargs: if cb nextargs is set, the next time cb is called these args will be
                         passed instead
        :param buf: if cb buf is not None, the cmd['output'] buffer will be appended with this
                    buf instead of std-out/err
        :param sendstring: ssh.cmd() will send this string to the channel if not None
        :param nextcb: optional callback can be return to ssh.cmd() to handle future output
                      rx'd on the channel
        :param removecb: boolean used to remove any callback from future output for ssh.cmd()
        """
        self.stop = stop
        self.statuscode = statuscode
        self.settimer = settimer
        self.sendstring = sendstring
        self.nextargs = nextargs or []
        self.nextcb = nextcb
        self.removecb = removecb
        self.buf = buf


class SshConnection():
    cmd_timeout_err_code = -100
    cmd_not_executed_code = -99

    def __init__(self,
                 host,
                 username='root',
                 password=None,
                 keypair=None,
                 keypath=None,
                 proxy=None,
                 proxy_username='root',
                 proxy_password=None,
                 proxy_keyname=None,
                 proxy_keypath=None,
                 key_files=None,
                 find_keys=True,
                 enable_ipv6_dns=False,
                 timeout=60,
                 banner_timeout=None,
                 retry=1,
                 logger=None,
                 verbose=False,
                 debug_connect=False):
        """
        :param host: -mandatory - string, hostname or ip address to establish ssh connection to
        :param username: - optional - string, username used to establish ssh session when keypath
                                     is not provided
        :param password: - optional - string, password used to establish ssh session when keypath
                                      is not provided
        :param keypair: - optional - boto keypair object, used to attept to derive local path to
                                    ssh key if present
        :param keypath:  - optional - string, path to ssh key
        :param proxy: - optional - host to proxy ssh connection through
        :param proxy_username:  - optional ssh username of proxy host for authentication
        :param proxy_password: - optional ssh password of proxy host for authentication
        :param proxy_keypath: - optional path to ssh key to use for proxy authentication
        :param key_files: - optional ',' comma delimited list of key file paths
        :param proxy_keyname: - optional keyname for proxy authentication, will attempt to derive
                               keypath from this
        :param enable_ipv6_dns: - optional - boolean to allow ipv6 dns hostname resolution
        :param timeout: - optional - integer, tcp timeout in seconds
        :param retry: - optional - integer, # of attempts made to establish ssh session without
                        auth failures
        :param logger: - method, used to handle debug msgs
        :param verbose: - optional - boolean to flag debug output on or off mainly for
                        cmd execution
        :param debug_connect: - optional - boolean to flag debug output on or off for connection
                                related operations
        """
        if not host:
            raise ValueError('SshConnection.__init__(). Hostname not populated:"{0}"'.format(host))
        self.host = host
        self.username = username
        self.password = password
        self.keypair = keypair
        self.keypath = keypath
        self.proxy = proxy
        self.proxy_username = proxy_username
        self.proxy_password = proxy_password
        self.proxy_keyname = proxy_keyname
        self.proxy_keypath = proxy_keypath
        self.enable_ipv6_dns = enable_ipv6_dns
        self.timeout = timeout
        self.banner_timeout = banner_timeout
        self.retry = retry
        self.log = logger or Eulogger(host)
        self.verbose = verbose
        self._sftp = None
        self.key_files = key_files or []
        if not isinstance(self.key_files, types.ListType):
            self.key_files = str(self.key_files).split(',')
        self.find_keys = find_keys
        self.debug_connect = debug_connect
        self._http_connections = {}

        # Used to store the last cmd attempted and it's exit code
        self.lastcmd = ""
        self.lastexitcode = SshConnection.cmd_not_executed_code

        if self.keypair is not None:
            self.keypath = os.getcwd() + "/" + self.keypair.name + ".pem"
        if self.keypath is not None:
            self.debug("SSH connection has hostname:" + str(self.host) + " user:" +
                       str(self.username) + " and keypath: " + str(self.keypath))
        else:
            self.debug("SSH connection has hostname:" + str(self.host) + " user:" +
                       str(self.username) + " password:" + str(self.mask_password(password)))
        if proxy:
            if self.proxy_keyname is not None:
                self.proxy_keypath = os.getcwd() + "/" + self.proxy_keyname + ".pem"
            if self.proxy_keypath is not None:
                self.debug("SSH proxy has hostname:" + str(self.proxy) + " user:" +
                           str(self.proxy_username) + " and keypath: " + str(self.proxy_keypath))
            else:
                self.debug("SSH proxy has hostname:" + str(self.proxy) + " user:" +
                           str(proxy_username) + " password:" +
                           str(self.mask_password(proxy_password)))

        if self.find_keys or \
                self.keypath is not None or \
                ((self.username is not None) and (self.password is not None)):
            self.connection = self.get_ssh_connection(self.host,
                                                      username=self.username,
                                                      password=self.password,
                                                      keypath=self.keypath,
                                                      proxy_username=self.proxy_username,
                                                      proxy_password=self.proxy_password,
                                                      proxy_keypath=self.proxy_keypath,
                                                      enable_ipv6_dns=self.enable_ipv6_dns,
                                                      timeout=self.timeout,
                                                      banner_timeout=self.banner_timeout,
                                                      retry=self.retry,
                                                      verbose=self.debug_connect)
        else:
            raise Exception("Need either a keypath or username+password to create ssh connection")

    def __repr__(self):
        return "{0}:{1}".format(self.__class__.__name__, self.host)

    def get_proxy_transport(self,
                            proxy_host=None,
                            dest_host=None,
                            port=22,
                            proxy_username='root',
                            proxy_password=None,
                            proxy_keypath=None,
                            key_files=None,
                            verbose=True):
        """


        :param key_files: pubkey file. If 'None' will check global self.key_files
                          default:'~/.ssh/authorized_keys'
        :param verbose: print debug
        :param proxy_host: hostname of ssh proxy
        :param port: ssh proxy port
        :param dest_host: end host to connect to
        :param proxy_username: proxy username for ssh authentication
        :param proxy_password: proxy password for ssh authentication
        :param proxy_keypath: local path to key used for ssh authentication
        :return: paramiko transport
        """
        proxy_host = ((proxy_host or self.proxy), port)
        dest_host = ((dest_host or self.host), port)
        proxy_username = proxy_username or self.proxy_username
        proxy_password = proxy_password or self.proxy_password
        proxy_keypath = proxy_keypath or self.proxy_keypath
        key_files = key_files or self.key_files or []
        if key_files and not isinstance(key_files, types.ListType):
            key_files = key_files.split(',')

        # Make sure there is at least one likely way to authenticate...
        print 'PRoxy connect using password:{0} username:{1}'.format(proxy_password, proxy_username)
        if ((proxy_username is not None) and
                (key_files or self.find_keys or
                 proxy_keypath is not None or
                 proxy_password is not None)):
            p_transport = paramiko.Transport(proxy_host)
            p_transport.start_client()
            if proxy_keypath:
                priv_key = paramiko.RSAKey.from_private_key_file(proxy_keypath)
                p_transport.auth_publickey(proxy_username, priv_key)
            elif proxy_password:
                p_transport.auth_password(proxy_username, proxy_password)
            else:
                host, port = proxy_host
                #p_transport = paramiko.Transport(proxy_host)
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                print 'Attempting ssh transport connect: {0}'.format(proxy_host)
                ssh.connect(hostname=host, username=proxy_username, port=port)
                #ssh._transport = p_transport
                #self.debug("Proxy auth -Using local keys, no keypath/password provided",
                #           verbose=verbose)
                #ssh._auth(proxy_username, None, None, key_files, True, True)
                #ssh._auth(username=proxy_username, password=proxy_password, pkey=proxy_keypath,
                #          key_filenames=key_files, allow_agent=True, look_for_keys=True,
                #          gss_auth=True, gss_kex=True, gss_deleg_creds=True, gss_host=True)
                print 'done with connect'
                p_transport = ssh._transport

                #p_transport.connect(username=proxy_username)
            # forward from 127.0.0.1:<free_random_port> to |dest_host|

            channel = p_transport.open_channel('direct-tcpip', dest_host, ('127.0.0.1', 0))
            return paramiko.Transport(channel)
        else:
            raise Exception("Need either a keypath or username+password to create ssh "
                            "proxy connection")

    def debug(self, msg, verbose=None):
        """
        simple method for printing debug.
        :param msg: - mandatory - string to be printed
        :param verbose: boolean to override global verbose flag
        """
        if verbose is None:
            verbose = self.verbose
        if verbose is True:
            if self.log is None:
                print (str(msg))
            else:
                self.log.debug(msg)

    def ssh_sys_timeout(self, chan, start, cmd):
        """
        callback to be scheduled during ssh cmds which have timed out.
        :param chan: - paramiko channel to be closed
        :param start - time.time() used to calc elapsed time when this fired for debug
        :param cmd - the command ran
        """
        chan.close()
        elapsed = time.time() - start
        raise CommandTimeoutException(
            "SSH Command timer fired after " + str(int(elapsed)) + " seconds. Cmd:'" +
            str(cmd) + "'", elapsed=elapsed)

    def sys(self, cmd, verbose=False, timeout=120, listformat=True, enable_debug=False, code=None,
            check_alive=True, invoke_shell=False, get_pty=True,):
        """
        Issue a command cmd and return output

        :param cmd: - mandatory - string representing the command to be run  against the remote
                      ssh session
        :param verbose: - optional - will default to global setting, can be set per cmd() as
                          well here
        :param timeout: - optional - integer used to timeout the overall cmd() operation in
                          case of remote blockingd
        :param listformat:  - optional - format output into single buffer or list of lines

        :param code: - optional - expected exitcode, will except if cmd's  exitcode does not
                       match this value
        :param check_alive - optional - bool, If true will check if the transport is alive,
                             and re-establish it if not before attempting to send the command.
        :param get_pty: Request a pseudo-terminal from the server.
        :param invoke_shell: Request a shell session on this channel

        """
        out = self.cmd(cmd, verbose=verbose, timeout=timeout, listformat=listformat,
                       enable_debug=enable_debug, get_pty=get_pty, invoke_shell=invoke_shell,
                       check_alive=check_alive)
        output = out['output']
        if code is not None and out['status'] != code:
            if verbose:
                self.debug(output)
            raise CommandExitCodeException('Cmd:' + str(cmd) + ' failed with status code:' +
                                           str(out['status']) + ", output:" + str(output),
                                           status=out['status'])
        return output

    def cmd(self,
            cmd,
            verbose=None,
            timeout=120,
            listformat=False,
            enable_debug=False,
            cb=None, cbargs=[],
            invoke_shell=False,
            get_pty=True,
            shell_delay=2,
            check_alive=True,
            shell_return='\r'):
        """
        Runs a command 'cmd' within an ssh connection.
        Upon success returns dict representing outcome of the command.

        Returns dict:
            ['cmd'] - The command which was executed
            ['output'] - The std out/err from the executed command
            ['status'] - The exitcode of the command. Note in the case a call back fires, this
                         exitcode is unreliable.
            ['cbfired']  - Boolean to indicate whether or not the provided callback fired
                          (ie returned False)
            ['elapsed'] - Time elapsed waiting for command loop to end.
        Arguments:
        :param cmd: - mandatory - string representing the command to be run  against the
                      remote ssh session
        :param verbose: - optional - will default to global setting, can be set per cmd() as
                          well here
        :param timeout: - optional - integer used to timeout the overall cmd() operation in
                          case of remote blocking
        :param listformat: - optional - boolean, if set returns output as list of lines, else a
                             single buffer/string
        :param cb: - optional - callback, method that can be used to handle output as it's rx'd
                    instead of waiting for the cmd to finish and return buffer.
                    Called like: cb(ssh_cmd_out_buffer, *cbargs)
                    Must accept string buffer, and return an integer to be used as cmd status.
                    Must return type 'sshconnection.SshCbReturn'
                    If cb returns stop, recv loop will end, and channel will be closed.
                    if cb settimer is > 0, timer timeout will be adjusted for this time
                    if cb statuscode is != -1 cmd status will return with this value
                    if cb nextargs is set, the next time cb is called these args will be passed
                    instead of cbargs
        :param cbargs: - optional - list of arguments to be appended to output buffer and
                         passed to cb
        :param get_pty: Request a pseudo-terminal from the server.
        :param invoke_shell: Request a shell session on this channel
        :param enable_debug: - optional - boolean, if set will use self.debug() to print
                               additional messages during cmd()
        :param check_alive - optional - bool, If true will check if the transport is alive,
                             and re-establish it if not before attempting to send the command.
        """
        if verbose is None:
            verbose = self.verbose
        ret = {}
        cbfired = False
        cmd = str(cmd)
        self.lastcmd = cmd
        self.lastexitcode = SshConnection.cmd_not_executed_code
        start = time.time()
        status = None

        def cmddebug(msg):
            if enable_debug:
                self.debug(msg)
        if verbose:
            self.debug("[" + self.username + "@" + str(self.host) + "]# " + cmd)
        try:

            if check_alive and not self.is_alive():
                self.debug("SSH transport was not alive, attempting to restablish ssh to: " +
                           str(self.host))
                self.refresh_connection()

            tran = self.connection.get_transport()
            attempt = 0
            while not attempt:
                try:
                    chan = tran.open_session(timeout=10)
                    break
                except Exception as E:
                    if not attempt:
                        self.log.warning('CMD:"{0}", Error while opening channel:{0}'
                                         .format(cmd, E))
                        self.log.warning('Attempting to reconnect and open channel again...')
                        self.refresh_connection()
                        tran = self.connection.get_transport()
                        chan = tran.open_session(timeout=10)
                    else:
                        raise

            try:
                chan.settimeout(timeout)
                if get_pty or invoke_shell:
                    chan.get_pty()
                chan.setblocking(0)
                if invoke_shell:
                    if verbose:
                        self.debug('Invoking shell...')
                    chan.invoke_shell()
                    time.sleep(shell_delay)
                    cmd = cmd.rstrip() + shell_return
                    chan.send(cmd)
                else:
                    chan.exec_command(cmd)
                output = None
                fd = chan.fileno()
            except:
                if chan:
                    chan.close()
                raise
            cmdstart = start = time.time()
            newdebug = "\n"
            while not chan.closed:
                time.sleep(0.05)
                try:
                    rl, wl, xl = select.select([fd], [], [], timeout)
                except select.error:
                    break
                elapsed = int(time.time() - start)
                if elapsed >= timeout and len(rl) < 1:
                    raise CommandTimeoutException(
                        "SSH Command timer fired after " + str(int(elapsed)) + " seconds. Cmd:'" +
                        str(cmd) + "'", elapsed=elapsed)
                if len(rl) > 0:
                    cmddebug('ssh cmd: got input on recv channel')
                    while chan.recv_ready():
                        new = chan.recv(1024)
                        if verbose:
                            cmddebug('ssh cmd: got new data on channel:"' + str(new) + '"')
                        if new is not None:
                            # We have data to handle...
                            # Run call back if there is one, let call back handle data read in
                            if cb is not None:
                                if enable_debug:
                                    cbname = 'unknown'
                                    try:
                                        cbname = str(cb.im_func.func_code.co_name)
                                    except:
                                        pass
                                    self.debug('ssh cmd: sending new data to callback: ' +
                                               str(cbname))
                                # If cb returns false break, end rx loop, return cmd
                                # outcome/output dict.
                                # cbreturn = SshCbReturn()
                                cbreturn = cb(new, *cbargs)
                                # Let the callback control whether or not to continue
                                if cbreturn.stop:
                                    cmddebug('ssh cmd: callback sent stop')
                                    if cbreturn.buf:
                                        if output is None:
                                            output = cbreturn.buf
                                        else:
                                            output += cbreturn.buf
                                    cbfired = True
                                    chan.close()
                                    # Let the callback dictate the return code, otherwise -1 for
                                    # connection err may occur
                                    if cbreturn.statuscode != -1:
                                        status = cbreturn.statuscode
                                    else:
                                        status = self.lastexitcode = chan.recv_exit_status()
                                    break
                                else:

                                    # Let the callback update its calling args if needed
                                    if cbreturn.nextargs is not None:
                                        cbargs = cbreturn.nextargs
                                    # Let the callback update/reset the timeout if needed
                                    if cbreturn.settimer > 0:
                                        start = time.time()
                                        timeout = cbreturn.settimer
                                    # Let the callback update the output buffer to be returned
                                    if cbreturn.buf:
                                        cmddebug('ssh cmd: cb returned buf:"' + str(cbreturn.buf) +
                                                 '"')
                                        if output is None:
                                            output = cbreturn.buf
                                        else:
                                            output += cbreturn.buf
                                    # Change the callback to handle future output from this cmd
                                    if cbreturn.nextcb:
                                        cmddebug('ssh cmd: updating to new callback provided in '
                                                 'cb return nextcb')
                                        cb = cbreturn.nextcb
                                    # Remove all callbacks
                                    if cbreturn.removecb:
                                        cmddebug('ssh cmd: removing all callbacks per cb return '
                                                 'removecb value')
                                        cb = None
                                    # Send a string to the channel provided in callback
                                    # (similar to expect)
                                    if cbreturn.sendstring is not None:
                                        if verbose:
                                            cmddebug('Sending string:' + str(cbreturn.sendstring))
                                        chan.send(s=str(cbreturn.sendstring))
                                        cmddebug('channel status after sending string. '
                                                 'Is closed = ' + str(chan.closed))
                            else:
                                # if no call back then append output to return dict
                                # and handle debug
                                if output is None:
                                    output = new
                                else:
                                    output += new
                                if verbose:
                                    # Dont print line by line output if cb is used,
                                    # let cb handle that
                                    newdebug += new
                        else:
                            status = self.lastexitcode = chan.recv_exit_status()
                            chan.close()
                            break
                    if newdebug and verbose:
                        self.debug(str(newdebug))
                        newdebug = ''
                elif enable_debug:
                    self.debug('ssh cmd: len of rl was < 0')
            cmddebug('ssh cmd: channel closed')
            if output is None:
                output = ""
            if listformat:
                # return output as list of lines
                output = output.splitlines()
                if output is None:
                    output = []

            # add command outcome in return dict.
            if status is None:
                status = self.lastexitcode = chan.recv_exit_status()
            ret['cmd'] = cmd
            ret['output'] = output
            ret['status'] = status
            ret['cbfired'] = cbfired
            ret['elapsed'] = int(time.time() - cmdstart)
            if verbose:
                self.debug("done with exec")
        except CommandTimeoutException, cte:
            self.lastexitcode = SshConnection.cmd_timeout_err_code
            elapsed = str(int(time.time() - start))
            self.debug("Command (" + cmd + ") timeout exception after " + str(elapsed) +
                       " seconds\nException")
            raise cte
        return ret

    def is_alive(self):
        """
        Return info on whether transport is alive.
        :return: bool
        """
        try:
            if self.connection:
                transport = self.connection.get_transport()
                if transport:
                    transport.send_ignore()
                    return transport.isAlive() and transport.is_active()
            return False
        except EOFError, e:
            return False

    def refresh_connection(self):
        """
        Attempts to establish a new ssh connection to replace the old 'connection' of this
        ssh obj.
        """
        if self.connection:
            self.connection.close()
        self.connection = self.get_ssh_connection(self.host,
                                                  username=self.username,
                                                  password=self.password,
                                                  keypath=self.keypath,
                                                  proxy_username=self.proxy_username,
                                                  proxy_password=self.proxy_password,
                                                  proxy_keypath=self.proxy_keypath,
                                                  enable_ipv6_dns=self.enable_ipv6_dns,
                                                  timeout=self.timeout,
                                                  banner_timeout=self.banner_timeout,
                                                  retry=self.retry,
                                                  verbose=self.debug_connect)

    def get_ssh_connection(self,
                           hostname,
                           username="root",
                           password=None,
                           keypath=None,
                           proxy=None,
                           proxy_username=None,
                           proxy_password=None,
                           proxy_keypath=None,
                           key_files=None,
                           enable_ipv6_dns=None,
                           port=22,
                           timeout=60,
                           banner_timeout=60,
                           retry=1,
                           verbose=False):
        """
        Create a paramiko ssh session to hostname. Will attempt to authenticate first with a
        keypath if provided, if the sshkey file path is not provided.
        username and password will be used to authenticate. This leaves out the case where a
        password is passed as the password needed to unlock the key file. This 3rd case may
        need to be added but may mask failures in tests for key insertion when using tests
        who's images have baked in passwords for login access(tbd).
        Upon success returns a paramiko sshclient with an established connection.

        :param hostname: - mandatory - hostname or ip to establish ssh connection with
        :param username: - optional - username used to authenticate ssh session
        :param password: - optional - password used to authenticate ssh session
        :param keypath: - optional - full path to sshkey file used to authenticate ssh session
        :param proxy: - optional - host to proxy ssh connection through
        :param proxy_username:  - optional ssh username of proxy host for authentication
        :param proxy_password: - optional ssh password of proxy host for authentication
        :param proxy_keypath: - optional path to ssh key to use for proxy authentication
        :param timeout: - optional - tcp timeout
        :param enable_ipv6_dns: - optional - boolean to avoid ipv6 dns 'AAAA' lookups
        :param retry: - optional - Number of attempts to establish ssh connection for errors
                        outside of authentication
        :param port: - optional - port to connect to, default 22
        :param verbose: - optional - enable verbose debug output
        """
        if not hostname:
            raise ValueError('get_ssh_connection. Hostname not populated:"{0}"'.format(hostname))
        connected = False
        iplist = []
        ip = None
        key_files = key_files or self.key_files or []
        if key_files and not isinstance(key_files, types.ListType):
            key_files = key_files.split(',')
        proxy_ip = None
        if not key_files and password is None and keypath is None and not self.find_keys:
            raise Exception("ssh_connect: Need to set password, keypath, keyfiles, or find_keys")
        if enable_ipv6_dns is None:
            enable_ipv6_dns = self.enable_ipv6_dns
        proxy = proxy or self.proxy

        self.debug("ssh_connect args:\nhostname:" + str(hostname) +
                   "\nusername:" + str(username) +
                   "\npassword:" + str(password) +
                   "\nkeypath:" + str(keypath) +
                   "\nproxy_username:" + str(proxy_username) +
                   "\nproxy_password" + str(proxy_password) +
                   "\nproxy_keypath" + str(proxy_keypath) +
                   "\ntimeout:" + str(timeout) +
                   "\nretry:" + str(retry), verbose=verbose)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        hostname = str(hostname.strip())
        if not enable_ipv6_dns:
            self.debug('IPV6 DNS lookup disabled, do IPV4 resolution and pass IP to connect()',
                       verbose=verbose)
            # Paramiko uses family type 'AF_UNSPEC' which does both ipv4/ipv6 lookups and can
            # cause some DNS servers
            # to fail in their response(s). Hack to avoid ipv6 lookups...
            # Try ipv4 dns resolution of 'hostname', and pass the ip instead of a hostname to
            # Paramiko's connect to avoid the potential ipv6 'AAAA' lookup...
            iplist = get_ipv4_lookup(hostname, verbose=verbose)
        if not iplist:
            iplist = [hostname]
        attempt = 0
        # adjust retry count for debug 'readability' ie 'attempt 1' vs 'attempt 0'
        retry += 1
        while (attempt < retry) and not connected:
            attempt += 1
            proxy_transport = None
            for ip in iplist:
                if self.proxy:
                    if not enable_ipv6_dns:
                        proxy_ip = get_ipv4_lookup(self.proxy, debug_method=self.debug,
                                                   verbose=verbose)[0]
                        proxy_transport = self.get_proxy_transport(proxy_host=proxy,
                                                                   dest_host=ip,
                                                                   port=port,
                                                                   proxy_username=proxy_username,
                                                                   proxy_password=proxy_password,
                                                                   proxy_keypath=proxy_keypath)
                if proxy_transport:
                    ssh._transport = proxy_transport
                else:
                    ssh._transport = paramiko.Transport(ip)
                ssh._transport.start_client()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                try:
                    self.debug("SSH connection attempt(" + str(attempt) + " of " + str(retry) +
                               "), host:'" + str(username) + "@" + str(hostname) +
                               "', using ipv4:" + str(ip) +
                               ", thru proxy:'" + str(proxy_ip) + "'")
                    if keypath is None and password:
                        self.debug("Using username:" + username + " and password:" +
                                   str(self.mask_password(password)),
                                   verbose=verbose)
                        ssh._transport.auth_password(username, password)
                        # ssh.connect(ip, username=username, password=password, timeout=timeout)
                        connected = True
                        break
                    elif keypath:
                        self.debug("Using Keypath:" + keypath, verbose=verbose)
                        priv_key = paramiko.RSAKey.from_private_key_file(keypath)
                        ssh._transport.auth_publickey(username, priv_key)
                        # ssh.connect(ip, port=port, username=username, key_filename=keypath,
                        #             timeout=timeout)
                        connected = True
                        break
                    elif key_files or self.find_keys:
                        self.debug("Using local keys, no keypath/password provided.",
                                   verbose=verbose)
                        # ssh._auth(username, password, None, key_files, True, True)
                        ssh.connect(ip, port=port, username=username, key_filename=keypath,
                                    timeout=timeout, banner_timeout=banner_timeout)
                        connected = True

                except paramiko.ssh_exception.SSHException, se:
                    self.debug("Failed to connect to " + hostname + ", retry in 10 seconds. "
                               "Err:" + str(se))
                    time.sleep(10)
                    pass
            if connected:
                via_string = ''
                if proxy_transport:
                    proxy_host, port = ssh._transport.getpeername()
                    via_string = ' via proxy host:' + str(proxy_host) + ':' + str(port)
                self.debug('SSH - Connected to ' + str(ip) + str(via_string))
                break
        if not connected:
            raise Exception(
                'Failed to connect to "' + str(hostname) + '", attempts:' + str(attempt) +
                ". IPs tried:" + ",".join(iplist))
            # self.debug("Returning ssh connection to: "+ hostname)
        return ssh

    def mask_password(self, pass_string):
        """
        Replace all but first and last chars with '*' of provided password string.

        :param pass_string: string representing a password to hide/format
        :return: Formatted hidden password
        """
        password = copy.copy(pass_string)
        show = ""
        if not password:
            return password
        if len(password) > 3:
            length = len(password)-2
        else:
            length = len(password)
        for x in xrange(length):
            show += '*'
        if len(password) > 3:
            show = password[0]+show
            show += password[len(password)-1]
        return show

    def start_interactive(self, timeout=180):
        '''
        Example method to invoke an interactive shell
        :pararm timeout: inactive session timeout, a value of 0 will wait for input/output forever
        '''
        tran = self.connection.get_transport()
        if tran is None:
            self.debug("SSH transport was None, attempting to re-establish ssh to: " +
                       str(self.host))
            self.refresh_connection()
            tran = self.connection.get_transport()
        chan = tran.open_session()
        chan.get_pty()
        chan.setblocking(0)
        print('Opened channel, starting interactive mode...')
        oldtty = termios.tcgetattr(sys.stdin)
        try:
            tty.setraw(sys.stdin.fileno())
            tty.setcbreak(sys.stdin.fileno())
            chan.settimeout(0)
            chan.invoke_shell()
            fd = chan.fileno()
            while True:
                time.sleep(0.05)
                try:
                    read_ready, wlist, xlist = select.select([fd, sys.stdin], [], [], timeout)
                except select.error, se:
                    print 'select error:' + str(se)
                    break
                if fd in read_ready:
                    try:
                        recv = chan.recv(1024)
                        if recv is None or len(recv) == 0:
                            self.debug('Session closing (chan)...   ')
                            break
                        sys.stdout.write(recv)
                        sys.stdout.flush()
                    except socket.timeout:
                        pass
                elif sys.stdin in read_ready:
                    user_input = sys.stdin.read(1)
                    if user_input is None or len(user_input) == 0:
                        self.debug('Session closing (stdin)...')
                        break
                    chan.send(user_input)
                else:
                    self.debug('Got nothing, closing...')
                    break
        finally:
            try:
                termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)
            except:
                pass
            if chan:
                chan.close()

    @property
    def sftp(self):
        if self._sftp:
            if self._sftp.sock and not self._sftp.sock.closed:
                return self._sftp
        else:
            self._sftp = self.open_sftp()
        return self._sftp

    @sftp.setter
    def sftp(self, sftp):
        if isinstance(sftp, SFTPifc) or sftp is None:
            self._sftp = sftp
        else:
            raise ValueError('sftp must be of types; None or {0}, got:"{1}/{2}"'
                             .format(SFTPifc.__class__.__name__, sftp, type(sftp)))

    def open_sftp(self, transport=None):
        transport = transport or self.connection._transport
        sftp = SFTPifc.from_transport(transport)
        sftp.debug = self.debug
        self._sftp = sftp
        return sftp

    def close_sftp(self):
        self.sftp.close()

    def sftp_put(self, localfilepath, remotefilepath):
        """
        sftp transfer file from localfilepath to remote system at remotefilepath
        :param localfilepath: path to file on local system
        :param remotefilepath: destination path for put on remote system
        """
        if not self.connection._transport:
            self.refresh_connection()
        transport = self.connection._transport
        self.open_sftp()
        self.sftp.put(remotepath=remotefilepath, localpath=localfilepath)
        self.close_sftp()

    def sftp_get(self, localfilepath, remotefilepath):
        """
        sftp transfer file from remotefilepath to remote system at localfilepath
        :param localfilepath: path where remote file 'get' will place file on local system
        :param remotefilepath: destination path for file to 'get' on remote system
        """
        if not self.connection._transport:
            self.refresh_connection()
        transport = self.connection._transport
        self.open_sftp()
        self.sftp.get(remotepath=remotefilepath, localpath=localfilepath)
        self.close_sftp()

    def close(self):
        self.connection.close()

    def _get_local_unused_port(self, start=8500, checklimit=100):
        """
        Test a range of local ports starting from int 'start' to 'start+checklimit'.
        Returns the int of the first available port.

        :param start: int, the port to start checking from
        :param checklimit: The number of ports to check (until an available one
                           is found) starting from 'start'.
        :returns : int representing the first available port
        """
        for port in xrange(start, (start+checklimit)):
            if self._can_connect_to_local_port(port, addr='127.0.0.1'):
                return port
        raise ValueError('Could not find an available local port in range: {0} - {1}'
                         .format(start, start+checklimit))

    def _can_connect_to_local_port(self, port, addr='127.0.0.1'):
        """
        Test to see if a local port is available

        :param port:
        :param addr:
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((addr, port))
        except:
            return False
        finally:
            sock.close()
        if result == 0:
            # Couldnt connect to this socket, dont use it
            return True
        # could connect
        return False

    def _get_dict_id(self, dict_to_hash):
        """
        Creates a somewhat unique value from a dictionary of values.
        The intent is to provide an id for a unique set of dictionary values.
        :returns int
        """
        return int(abs(reduce(lambda x, y: x ^ y,
                              [hash(item) for item in dict_to_hash.items()])))

    def create_http_fwd_connection(self, destport, dest_addr='127.0.0.1', peer=None,
                                   localport=None, trans=None, httpaddr='127.0.0.1',
                                   do_cache=False, **connection_kwargs):
        """
        Create an http connection with port fowarding over this ssh session.

        :param destport: port to forward (ie 80 for http)
        :param dest_addr: addr used for remote request
        :param peer: Remote host
        :param localport: Local port used to forward
        :param trans: ssh transport obj
        :param httpaddr: addr used for http connection
        :returns HTTP connection obj
        """
        trans = trans or self.connection._transport
        assert isinstance(trans, paramiko.Transport)
        if peer is None:
            peer = trans.getpeername()[0]
        connection_kwargs = connection_kwargs or {}
        local_arg_dict = {'destport': destport,
                           'dest_addr': dest_addr,
                           'peer': peer,
                           'localport': localport,
                           'trans': trans,
                           'httpaddr': httpaddr,
                            }
        local_arg_dict.update(connection_kwargs)
        connection_id = self._get_dict_id(local_arg_dict)
        # If there is an existing connection return it
        if connection_id in self._http_connections.keys():
            http = self._http_connections[connection_id]
            if http.sock is not None:
                return {'connection': self._http_connections[connection_id],
                        'id': connection_id}
            else:
                del self._http_connections[connection_id]
        if localport is None:
            localport = self._get_local_unused_port(start=9000)
        self.debug('Making forwarded request from "localhost:{0}" to "{1}:{2}"'
                   .format(localport, peer, destport))
        self.debug('open_channel(kind="{0}", dest_addr=("{1}", {2}), src_addr=("{3}", {4})'
                   .format('direct-tcpip', dest_addr, destport, peer, localport))
        chan = trans.open_channel(kind='direct-tcpip', dest_addr=(dest_addr, destport),
                                  src_addr=(peer, localport))

        connection_kwargs['host'] = httpaddr
        connection_kwargs['port'] = destport
        self.debug('Creating HTTP connection with kwargs:\n{0}\n'.format(connection_kwargs))
        http = HTTPConnection(**connection_kwargs)
        http.sock = chan
        if do_cache:
            self._http_connections[connection_id] = http
        return {'connection': http, 'id': connection_id}

    def http_fwd_request(self, url, body=None, headers={}, method='GET', trans=None,
                         localport=9797, destport=None, cache_connnection=False):
        """
        Attempts to forward a single http request over the current ssh session.

        :param url: URL to use in the reuqest ie
        :param body: http request body
        :param headers: http request headers
        :param method: http request method, default: 'GET'
        :param trans: ssh transport obj
        :param localport:  Local port used to forward
        :param destport: port to forward (ie 80 for http), default is derived from the provided url
                         if present, otherwise port 80.
        :returns Http response obj

        Example:
            # Make a request to midonet api hosted at 10.111.5.156, over an session.
            # This will appear on the remote server as a request to port 8080 from it's
            # localhost...
            ssh = SshConnection(host='10.111.5.156', password='foobar', verbose=True)
            url = 'http://127.0.0.1:8080/midonet-api/routers/'
            response = ssh.http_fwd_request(url)
            print response.status
                 200
            data = response.read()
        """
        # Todo - Remove the sudo connection caching here(bad), and use http connection pools
        if destport is None:
            urlp = urlparse(url)
            destport = urlp.port or 80
        conn_dict = self.create_http_fwd_connection(destport=destport, dest_addr='127.0.0.1',
                                                    httpaddr='127.0.0.1', localport=localport,
                                                    do_cache=cache_connnection)
        http = conn_dict.get('connection')
        conn_id = conn_dict.get('id')
        try:
            req = http.request(method=method, url=url, body=body, headers=headers)
        except CannotSendRequest:
            if conn_id in self._http_connections:
                del self._http_connections[conn_id]
            raise
        status = getattr(req, 'status', None)
        if status:
            self.debug('{0}:{1}, req status:{2}'.format(method, url, status))
        resp = http.getresponse()
        status = getattr(resp, 'status', None)
        if status:
            self.debug('{0}:{1}, resp status:{2}'.format(method, url, status))
        return resp


class CommandExitCodeException(Exception):
    def __init__(self, value, status=None):
        self.value = value
        self.status = status

    def __str__(self):
        return repr(self.value)


class CommandTimeoutException(Exception):
    def __init__(self, value, elapsed=None):
        self.value = value
        self.elapsed = elapsed

    def __str__(self):
        return repr(self.value)
