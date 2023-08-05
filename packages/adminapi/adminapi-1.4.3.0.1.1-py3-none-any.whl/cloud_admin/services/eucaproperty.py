
from cloud_admin.services import EucaBaseObj
from cloud_utils.log_utils import get_traceback
from cloud_utils.log_utils import markup
import re
from prettytable import PrettyTable, ALL
from sre_constants import error

def SHOW_PROPERTIES(connection, properties=None, description=True, defaults=True, readonly=True,
                    grid=ALL, print_method=None, print_table=True, search=None, *nameprefix):
    """
    Summarize Eucalyptus properties in table format

    :param connection: EucaAdmin connection
    :param properties: list of property names, or Eucaproperties to summarize
    :param description: bool, show property descriptions
    :param grid: bool, show table in grid format
    :param readonly: bool, show readonly flag
    :param defaults: bool, show property defaults in table
    :param print_table: bool, if True will print table using connection.debug_method()
                        if False will return the table object
    :param search: string, to use as filter for name of properties
    :param nameprefix: property names used to filter query response
    """
    print_method = print_method or connection._show_method
    name_hdr = markup('PROPERTY NAME', [1, 94])
    def_hdr = markup('DEFAULT', [1, 94])
    value_hdr = markup('PROPERTY VALUE', [1, 94])
    desc_hdr = markup('DESCRIPTION', [1, 94])
    ro_hdr = markup('RO', [1, 94])
    pt = PrettyTable([name_hdr, value_hdr])
    pt.max_width[name_hdr] = 70
    pt.max_width[value_hdr] = 40

    if defaults:
        pt.add_column(fieldname=def_hdr, column=[])
        pt.max_width[def_hdr] = 40
    if readonly:
        pt.add_column(fieldname=ro_hdr, column=[])
    if description:
        pt.add_column(fieldname=desc_hdr, column=[])
        pt.max_width[desc_hdr] = 40
        # Reduce the default width to accommodate the description
        pt.max_width[def_hdr] = 20

    pt.padding_width = 0
    pt.align = 'l'
    pt.hrules = grid or 0
    if not isinstance(properties, list):
        properties = properties or connection.get_properties(search=search, *nameprefix)
    if not isinstance(properties, list):
        properties = [properties]
    for prop in properties:
        if not isinstance(prop, EucaProperty) and isinstance(prop, basestring):
            props = connection.get_properties(prop)
            if not props:
                continue
        else:
            props = [prop]
        for p in props:
            row = [markup(p.name, [94]), p.value]
            if defaults:
                row.append(getattr(p, 'defaultvalue', None))
            if readonly:
                ro = getattr(p, 'readonly', "?")
                if ro != "?":
                    if 'rue' in ro:
                        ro = 'T'
                    if 'alse' in ro:
                        ro = 'F'
                row.append(ro)
            if description:
                row.append(p.description)
            pt.add_row(row)
    if not pt._rows:
        err_row = [markup('NO PROPERTIES RETURNED', [1, 91])]
        for x in xrange(1, len(pt._field_names)):
            err_row.append("")
        pt.add_row(err_row)
    if print_table:
        print_method('\n' + str(pt) + '\n')
    else:
        return pt


def SHOW_PROPERTIES_NARROW(connection, properties=None, verbose=True, print_method=None,
                           print_table=True, *prop_names):
    """
    Narrow formatted table used to summarize Eucalyptus properties

    :param connection: EucaAdmin connection
    :param properties: list of EucaProperty objs or string names of properties
    :param verbose: show debug information during table creation
    :param print_table: bool, if True will print table using connection.debug_method()
                        if False will return the table object
    :param prop_names: property names used to filter query response
    """
    if not verbose:
        return connection.show_properties(properties=properties, description=False,
                                          print_method=print_method, print_table=print_table)
    print_method = print_method or connection._show_method
    info_len = 60
    desc_len = 40
    markup_size = len(markup('\n'))
    properties = properties or connection.get_properties(prop_names)
    pt = PrettyTable(['PROPERTY INFO', 'DESCRIPTION'])
    pt.max_width['PROPERTY INFO'] = info_len
    pt.max_width['DESCRIPTION'] = desc_len
    pt.align = 'l'
    pt.padding_width = 0
    pt.hrules = 1
    if not isinstance(properties, list):
        properties = [properties]
    for prop in properties:
        if not isinstance(prop, EucaProperty) and isinstance(prop, basestring):
            props = connection.get_properties(prop)
            if not props:
                continue
        else:
            props = [prop]
        for p in props:
            info_buf = "NAME: "
            prefix = ""
            line_len = info_len - markup_size - len('NAME: ')
            for i in xrange(0, len(p.name), line_len):
                if i:
                    prefix = "      "
                info_buf += (str(prefix + markup(p.name[i:i+line_len], [1, 94]))
                             .ljust(info_len-2) + "\n")
            info_buf += 'VALUE: '
            prefix = ""
            line_len = info_len - markup_size - len('VALUE: ')
            for i in xrange(0, len(p.value), line_len):
                if i:
                    prefix = "       "
                info_buf += (prefix + markup(p.value[i:i+line_len]) + "\n")

            desc_buf = markup('DESCRIPTION:').ljust(desc_len) + str(p.description).ljust(desc_len)
            pt.add_row([info_buf, desc_buf])
    if not pt._rows:
        pt.add_row([markup('NO PROPERTIES RETURNED', [1, 91]), ""])
    if print_table:
        print_method("\n" + str(pt) + "\n")
    else:
        return pt


class EucaProperty(EucaBaseObj):
    # Base Class for Eucalyptus Properties
    def __init__(self, connection=None):
        super(EucaProperty, self).__init__(connection)
        self.value = None
        self._description = None

    def endElement(self, name, value, connection):
        ename = name.lower().replace('euca:', '')
        if ename == 'description':
            self.description = value
        elif ename == 'name':
            self.name = value
        elif ename == 'value':
            self.value = value
        elif ename:
            setattr(self, ename, value)

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        # Hack to prevent updates from overwriting description value
        if value and str(value).lower().strip() != 'none':
            self._description = value

    def show(self):
        return SHOW_PROPERTIES(self.connection, self)

    def update(self, new_prop=None, silent=True):
        """
        Updates this property obj
        :params silent: bool, if True will not raise Exceptions found during lookup, will instead
                        write errors to self.connection.err_method()
        :returns : self upon successful update, otherwise returns None
        """
        errmsg = ""
        if not new_prop:
            try:
                new_prop = self.connection.get_property(self)
            except Exception as LE:
                if silent:
                    errmsg = "{0}\n{1}\n".format(get_traceback(), str(LE))
                    self.connection.err_method('{0}Update failed for property:{1}'
                                               .format(errmsg, self.name))
                    return None
                else:
                    raise
        if not isinstance(new_prop, EucaProperty):
            raise ValueError('"{0}" update error. Non EucaProperty type for new_prop. Found: '
                             '"{1}/{2}"'.format(self.name, new_prop, type(new_prop)))
        if new_prop:
            self.__dict__.update(new_prop.__dict__)
            return self

    def modify_value(self, value, regex=None):
        """
        Modify this property's value.
        :param value: The new value to request this property be modified to.
        :param regex: regex used to validate resulting property value in response.
                      default regex will allow result to match 'value' or '*'+
        :returns: modified EucaProperty
        :raise: ValueError if modified property value does not match requested value
        """
        self.connection.modify_property(self, value)
        self.update()
        if regex is None:
            regex = "{0}|\*+".format(value)
        try:
            match = re.match(regex, self.value)
        except error as constants_error:
            self.connection.err_method('Trying string comparison due to regex error:"{0}"'
                                       .format(constants_error))
            if str(value).strip() == self.value.strip():
                match = True
        if not match:
            raise ValueError('Modified property value does not match expected regex:{0}, '
                             'current:{1}'.format(regex, self.value))
        return self
