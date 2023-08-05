import re
from dataclasses import dataclass, field, astuple
from typing import Literal


@dataclass
class FileObject:
    """
        A Tableau File object is any element in a Tableau Online/Server object that can be downloaded,
        i.e. Columns, Folders, Connections, etc, in Datasources/Workbooks.

        This is the base class for a Tableau File object,
        with the minimum required attributes and functionality.
        Child classes will inherit the functionality provided by this base class.

        The data types of attributes from child class will be converted to the appropriate type,
        if it is provided as a string instead.
    """
    def __existing_str_attr(self, attr: str):
        """ Returns: True if the attribute exists and is a string """
        return (
            hasattr(self, attr)
            and getattr(self, attr)
            and isinstance(getattr(self, attr), str)
        )

    def __to_int(self, attr: str):
        """
            Set the attribute to an integer,
            if the class has the attribute,
            and if the attribute is a string.
        """
        if self.__existing_str_attr(attr):
            setattr(self, attr, int(getattr(self, attr)))

    def __to_bool(self, attr: str):
        """
            Set the attribute to a boolean,
            if the class has the attribute,
            and if the attribute is a string.
        """
        if self.__existing_str_attr(attr):
            setattr(self, attr, getattr(self, attr).lower() == 'true')

    def __post_init__(self):
        # Convert to Boolean
        self.__to_bool('contains_null')
        self.__to_bool('datatype_customized')
        self.__to_bool('extract_engine')
        self.__to_bool('hidden')
        # Convert to Integer
        self.__to_int('approx_count')
        self.__to_int('collation_flag')
        self.__to_int('ordinal')
        self.__to_int('port')
        self.__to_int('precision')
        self.__to_int('scale')
        self.__to_int('width')


@dataclass
class Column(FileObject):
    """ The Column Tableau file object """
    name: str
    datatype: Literal['boolean', 'date', 'datetime', 'integer', 'real', 'string', 'table']
    role: Literal['dimension', 'measure']
    type: Literal['nominal', 'ordinal', 'quantitative']
    default_role: str = None
    default_type: str = None
    default_format: str = None
    ns0_auto_column: str = None
    xmlns_ns0: str = None
    semantic_role: str = None
    caption: str = None
    desc: str = None
    calculation: str = None
    aggregation: str = None
    user_auto_column: str = None
    param_domain_type: str = None
    value: str = None
    alias: str = None
    ordinal: int = None
    datatype_customized: bool = None
    hidden: bool = None
    aliases: list = None
    members: dict = None
    range: dict = None

    def __post_init__(self):
        if not re.match(r'^\[.+]$', self.name):
            self.name = f'[{self.name}]'
        if self.aliases and isinstance(self.aliases, dict):
            if isinstance(self.aliases['alias'], list):
                self.aliases = self.aliases['alias']
            else:
                self.aliases = [self.aliases['alias']]
        if self.desc and isinstance(self.desc, dict):
            self.desc = self.desc['formatted-text']['run']
        if self.calculation and isinstance(self.calculation, dict) and self.calculation['@class'] == 'tableau':
            self.calculation = self.calculation['@formula']
        elif self.calculation:
            self.calculation = None
        super().__post_init__()

    def __hash__(self):
        return hash(str(astuple(self)))

    def __eq__(self, other):
        name = ''
        if isinstance(other, str):
            name = other.lower()
        elif isinstance(other, dict):
            name = other.get('name').lower()
        elif isinstance(other, (Column, object)):
            name = other.name.lower()

        if not re.match(r'^\[.+]$', name):
            name = f'[{name}]'

        return self.name.lower() == name

    def dict(self):
        output = {
            '@name': self.name,
            '@datatype': self.datatype,
            '@role': self.role,
            '@type': self.type
        }
        if self.semantic_role:
            output['@semantic-role'] = self.semantic_role
        if self.ns0_auto_column:
            output['@ns0:auto-column'] = self.ns0_auto_column
        if self.xmlns_ns0:
            output['@xmlns:ns0'] = self.xmlns_ns0
        if self.default_format:
            output['@default-format'] = self.default_format
        if self.caption:
            output['@caption'] = self.caption
        if self.aggregation:
            output['@aggregation'] = self.aggregation
        if self.user_auto_column:
            output['@user:auto-column'] = self.user_auto_column
        if self.default_role:
            output['@default-role'] = self.default_role
        if self.default_type:
            output['@default-type'] = self.default_type
        if self.param_domain_type:
            output['@param-domain-type'] = self.param_domain_type
        if self.alias:
            output['@alias'] = self.alias
        if self.value:
            output['@value'] = self.value
        if self.ordinal is not None:
            output['@ordinal'] = str(self.ordinal)
        if self.members:
            output['members'] = self.members
        if self.range:
            output['range'] = self.range
        if self.hidden is not None:
            output['@hidden'] = str(self.hidden).lower()
        if self.datatype_customized is not None:
            output['@datatype-customized'] = str(self.datatype_customized).lower()
        if self.calculation:
            output['calculation'] = {'@class': 'tableau', '@formula': self.calculation}
        if self.desc:
            output['desc'] = {'formatted-text': {'run': self.desc}}
        if self.aliases:
            output['aliases'] = dict()
            output['aliases']['alias'] = self.aliases
        return output


@dataclass
class Relation(FileObject):
    name: str
    type: str
    table: str = None
    text: str = None
    connection: str = None

    def __hash__(self):
        return hash(str(astuple(self)))

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        if isinstance(other, dict):
            return self.name == other.get('name')
        if isinstance(other, (FolderItem, object)):
            return self.name == other.name
        return False

    def dict(self):
        dictionary = {
            '@name': self.name,
            '@type': self.type
        }

        if self.connection:
            dictionary['@connection'] = self.connection
        if self.table:
            dictionary['@table'] = self.table
        if self.text:
            dictionary['@text'] = self.text

        return dictionary


@dataclass
class MappingCol(FileObject):
    key: str
    value: str

    def __post_init__(self):
        if not re.match(r'^\[.+]$', self.key):
            self.key = f'[{self.key}]'
        if not re.match(r'^\[.+]$', self.value):
            table, column = self.value.split('.')
            self.value = f'[{table}].[{column}]'
        super().__post_init__()

    def __hash__(self):
        return hash(str(astuple(self)))

    def __eq__(self, other):
        key = ''
        if isinstance(other, str):
            key = other.lower()
        elif isinstance(other, dict):
            key = other.get('key').lower()
        elif isinstance(other, (MappingCol, object)):
            key = other.key.lower()

        if not re.match(r'^\[.+]$', key):
            key = f'[{key}]'

        return self.key.lower() == key

    def dict(self):
        return {'@key': self.key, '@value': self.value}


@dataclass
class FolderItem(FileObject):
    """ The FolderItem Tableau file object, is an Item of the Folder.folder_item list """
    name: str
    type: str = 'field'

    def __hash__(self):
        return hash(str(astuple(self)))

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        if isinstance(other, dict):
            return self.name == other.get('name') and self.type == other.get('type')
        if isinstance(other, (FolderItem, object)):
            return self.name == other.name and self.type == other.type
        return False

    def dict(self):
        return {'@name': self.name, '@type': self.type}


@dataclass
class Folder(FileObject):
    """ The Folder Tableau file object """
    name: str
    role: str = None
    folder_item: list[FolderItem] = field(default_factory=list)

    def __hash__(self):
        return hash(str(astuple(self)))

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        if self.role is not None:
            if isinstance(other, dict):
                return self.name == other.get('name') and self.role == other.get('role')
            if isinstance(other, (Column, object)):
                return self.name == other.name and self.role == other.role
        else:
            if isinstance(other, dict):
                return self.name == other.get('name')
            if isinstance(other, (Column, object)):
                return self.name == other.name
        return False

    def dict(self):
        output = {'@name': self.name}
        if self.role:
            output['@role'] = self.role
        if self.folder_item:
            output['folder-item'] = list()
            for folder_item in self.folder_item:
                output['folder-item'].append(folder_item.dict())
        return output


@dataclass
class Connection(FileObject):
    """ The Connection Tableau file object """
    class_name: str
    name: str
    caption: str = None
    dbname: str = None
    schema: str = None
    server: str = None
    service: str = None
    default_settings: str = None
    directory: str = None
    filename: str = None
    tablename: str = None
    username: str = None
    warehouse: str = None
    authentication: str = None
    odbc_connect_string_extras: str = None
    one_time_sql: str = None
    server_oauth: str = None
    workgroup_auth_mode: str = None
    extract_engine: bool = None
    port: int = None

    def __hash__(self):
        return hash(str(astuple(self)))

    def __eq__(self, other):
        if isinstance(other, str):
            return self.class_name == other
        if isinstance(other, dict):
            return self.class_name == other.get('class_name')
        if isinstance(other, (Connection, object)):
            return self.class_name == other.class_name
        return False

    def dict(self):
        output = {
            '@caption': self.caption,
            '@name': self.name,
            'connection': dict()
        }
        if self.authentication:
            output['connection']['@authentication'] = self.authentication
        if self.class_name:
            output['connection']['@class'] = self.class_name
        if self.dbname:
            output['connection']['@dbname'] = self.dbname
        if self.schema:
            output['connection']['@schema'] = self.schema
        if self.server:
            output['connection']['@server'] = self.server
        if self.service:
            output['connection']['@service'] = self.service
        if self.username:
            output['connection']['@username'] = self.username
        if self.warehouse:
            output['connection']['@warehouse'] = self.warehouse
        if self.odbc_connect_string_extras:
            output['connection']['@odbc-connect-string-extras'] = self.odbc_connect_string_extras
        if self.one_time_sql:
            output['connection']['@one-time-sql'] = self.one_time_sql
        if self.server_oauth:
            output['connection']['@server-oauth'] = self.server_oauth
        if self.workgroup_auth_mode:
            output['connection']['@workgroup-auth-mode'] = self.workgroup_auth_mode
        if self.tablename:
            output['connection']['@tablename'] = self.tablename
        if self.default_settings:
            output['connection']['@default-settings'] = self.default_settings
        if self.directory:
            output['connection']['@directory'] = self.directory
        if self.filename:
            output['connection']['@filename'] = self.filename
        if self.extract_engine is not None:
            output['connection']['@extract-engine'] = self.extract_engine
        if self.port is not None:
            output['connection']['@port'] = self.port
        return output


@dataclass
class MetadataRecord(FileObject):
    """ The MetadataColumn Tableau file object """
    class_name: str
    remote_name: str
    remote_type: str
    parent_name: str
    remote_alias: str
    local_name: str = None
    local_type: str = None
    object_id: str = None
    aggregation: str = None
    family: str = None
    collation_name: str = None
    contains_null: bool = None
    approx_count: int = None
    collation_flag: int = None
    ordinal: int = None
    precision: int = None
    scale: int = None
    width: int = None
    attributes: list = None

    def __post_init__(self):
        if isinstance(self.contains_null, str):
            self.contains_null = self.contains_null == 'true'
        if isinstance(self.scale, str):
            self.scale = int(self.scale)
        if isinstance(self.ordinal, str):
            self.ordinal = int(self.ordinal)
        if isinstance(self.precision, str):
            self.precision = int(self.precision)
        if isinstance(self.width, str):
            self.width = int(self.width)
        if isinstance(self.collation_flag, str):
            self.collation_flag = int(self.collation_flag)
        if self.attributes and isinstance(self.attributes, dict):
            self.attributes = self.attributes['attribute']
        super().__post_init__()

    def __hash__(self):
        return hash(str(astuple(self)))

    def __eq__(self, other):
        if isinstance(other, str):
            return self.remote_name == other
        if isinstance(other, dict):
            return self.remote_name == other.get('remote_name')
        if isinstance(other, (Column, object)):
            return self.remote_name == other.remote_name
        return False

    def dict(self):
        output = {
            '@class': self.class_name,
            'remote-name': self.remote_name,
            'remote-type': self.remote_type,
            'local-name': self.local_name,
            'parent-name': self.parent_name,
            'remote-alias': self.remote_alias,
            'local-type': self.local_type
        }

        if self.object_id:
            output['object-id'] = self.object_id
        if self.ordinal:
            output['ordinal'] = self.ordinal
        if self.aggregation:
            output['aggregation'] = self.aggregation
        if self.family:
            output['family'] = self.family
        if self.contains_null is not None:
            output['contains-null'] = self.contains_null
        if self.approx_count is not None:
            output['approx-count'] = self.approx_count
        if self.scale is not None:
            output['scale'] = self.scale
        if self.precision is not None:
            output['precision'] = self.precision
        if self.width is not None:
            output['width'] = self.width
        if self.collation_flag:
            output.setdefault('collation', dict())
            output['collation']['@flag'] = self.collation_flag
        if self.collation_name:
            output.setdefault('collation', dict())
            output['collation']['@name'] = self.collation_name
        if self.attributes:
            output['attributes'] = dict()
            output['attributes']['attribute'] = self.attributes
        return output


if __name__ == '__main__':
    t1 = Column(name='Test', datatype='integer', role='measure', type='quantitative', calculation='COUNT(1)')
    t2 = Column(name='Test', datatype='string', role='dimension', type='ordinal')
    print(t1 == 'Test')
    print(t1 == {'name': 'Test'})
    print(t1 == t2)
    print(t1.dict())
    print(t2.dict())
