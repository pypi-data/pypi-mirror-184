import xmltodict
from datetime import datetime
from dataclasses import dataclass, asdict, astuple


@dataclass
class ServerObject:
    """
        A Tableau Server object is any object in Tableau Online/Server,
        i.e. Datasources, Workbooks, Users, Groups, Projects, etc.

        This is the base class for a Tableau Server object,
        with the minimum required attributes and functionality.
        Child classes will inherit the functionality provided by this base class.

        The data types of attributes from child class will be converted to the appropriate type,
        if it is provided as a string instead.
    """
    id: str

    def __existing_str_attr(self, attr: str):
        """ Returns: True if the attribute exists and is a string """
        return hasattr(self, attr) and isinstance(getattr(self, attr), str)

    def __to_datetime(self, attr: str):
        """
            Set the attribute to a datetime,
            if the class has the attribute,
            and if the attribute is a string.
        """
        if self.__existing_str_attr(attr):
            setattr(self, attr, datetime.strptime(getattr(self, attr), '%Y-%m-%dT%H:%M:%SZ'))

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
        # Convert to Datetime
        self.__to_datetime('created_at')
        self.__to_datetime('completed_at')
        self.__to_datetime('last_login')
        self.__to_datetime('next_run_at')
        self.__to_datetime('updated_at')
        # Convert to Boolean
        self.__to_bool('attach_image')
        self.__to_bool('attach_pdf')
        self.__to_bool('content_send_if_view_empty')
        self.__to_bool('data_acceleration_config_acceleration_enabled')
        self.__to_bool('embed_password')
        self.__to_bool('encrypt_extracts')
        self.__to_bool('has_alert')
        self.__to_bool('has_extracts')
        self.__to_bool('is_certified')
        self.__to_bool('is_published')
        self.__to_bool('is_embedded')
        self.__to_bool('query_tagging_enabled')
        self.__to_bool('show_tabs')
        self.__to_bool('suspended')
        self.__to_bool('top_level_project')
        self.__to_bool('use_remote_query_agent')
        self.__to_bool('writeable')
        # Convert to Integer
        self.__to_int('connected_workbooks_count')
        self.__to_int('contents_counts_datasource_count')
        self.__to_int('contents_counts_project_count')
        self.__to_int('contents_counts_view_count')
        self.__to_int('contents_counts_workbook_count')
        self.__to_int('favorites_total')
        self.__to_int('finish_code')
        self.__to_int('port')
        self.__to_int('priority')
        self.__to_int('server_port')
        self.__to_int('sheet_count')
        self.__to_int('size')
        self.__to_int('usage_total_view_count')
        self.__to_int('user_count')

    def to_dict(self):
        return asdict(self)


@dataclass
class User(ServerObject):
    """ A Tableau User object """
    name: str
    full_name: str = None
    domain_name: str = None
    auth_setting: str = None
    email: str = None
    email_domain: str = None
    external_auth_user_id: str = None
    site_role: str = None
    locale: str = None
    language: str = None
    last_login: datetime = None

    def __post_init__(self):
        if not self.email_domain and self.email:
            self.email_domain = self.email.lower().split('@')[-1]
        super().__post_init__()

    def __hash__(self):
        return hash(str(astuple(self)))


@dataclass
class Project(ServerObject):
    """ A Tableau Project object """
    name: str
    owner_id: str = None
    parent_project_id: str = None
    description: str = None
    controlling_permissions_project_id: str = None
    created_at: datetime = None
    updated_at: datetime = None
    content_permissions: str = None
    top_level_project: bool = False
    writeable: bool = False
    contents_counts_project_count: int = None
    contents_counts_view_count: int = None
    contents_counts_datasource_count: int = None
    contents_counts_workbook_count: int = None

    def __hash__(self):
        return hash(str(astuple(self)))


@dataclass
class Group(ServerObject):
    """ A Tableau Group object """
    name: str
    domain_name: str = None
    import_domain_name: str = None
    import_site_role: str = None
    import_grant_license_mode: str = None
    minimum_site_role: str = None
    user_count: int = None

    def __hash__(self):
        return hash(str(astuple(self)))


@dataclass
class Datasource(ServerObject):
    """ A Tableau Datasource object """
    name: str
    created_at: datetime = None
    updated_at: datetime = None
    project_id: str = None
    project_name: str = None
    owner_id: str = None
    tags: list = None
    description: str = None
    content_url: str = None
    type: str = None
    encrypt_extracts: bool = False
    has_alert: bool = False
    has_extracts: bool = False
    is_certified: bool = False
    is_published: bool = True
    use_remote_query_agent: bool = False
    database_name: str = None
    server_name: str = None
    favorites_total: int = None
    connected_workbooks_count: int = None

    def __hash__(self):
        return hash(str(astuple(self)))

    def publish_xml(self, conn_creds=None):
        xml_dict = {
            'tsRequest': {
                'datasource': {
                    '@name': self.name,
                    '@useRemoteQueryAgent': str(self.use_remote_query_agent).lower(),
                    '@description': self.description,
                    'project': {'@id': self.project_id}
                }
            }
        }
        if conn_creds:
            xml_dict['tsRequest']['datasource']['connectionCredentials'] = {
                '@name': conn_creds['username'],
                '@password': conn_creds['password'],
                '@embed': "true"
            }
        return xmltodict.unparse(xml_dict)


@dataclass
class Connection(ServerObject):
    """ A Tableau Connection object """
    type: str
    datasource_id: str = None
    datasource_name: str = None
    workbook_id: str = None
    workbook_name: str = None
    user_name: str = None
    server_address: str = None
    server_port: int = None
    embed_password: bool = False
    query_tagging_enabled: bool = False

    def __hash__(self):
        return hash(str(astuple(self)))

    def to_dict(self):
        conn_dict = super().to_dict()
        del conn_dict['type']
        del conn_dict['datasource_id']
        del conn_dict['datasource_name']
        return conn_dict


@dataclass
class View(ServerObject):
    """ A Tableau View object """
    name: str
    created_at: datetime = None
    updated_at: datetime = None
    workbook_id: str = None
    owner_id: str = None
    project_id: str = None
    tags: list = None
    location_id: str = None
    location_type: str = None
    content_url: str = None
    view_url_name: str = None
    sheet_type: str = None
    usage_total_view_count: int = None

    def __hash__(self):
        return hash(str(astuple(self)))


@dataclass
class Workbook(ServerObject):
    """ A Tableau Workbook object """
    name: str
    created_at: datetime = None
    updated_at: datetime = None
    project_id: str = None
    project_name: str = None
    owner_id: str = None
    owner_name: str = None
    location_type: str = None
    location_name: str = None
    tags: list = None
    default_view_id: str = None
    description: str = None
    content_url: str = None
    webpage_url: str = None
    data_acceleration_config_acceleration_enabled: bool = False
    show_tabs: bool = False
    encrypt_extracts: bool = False
    has_extracts: bool = False
    views: list = None
    location_id: str = None
    size: int = 0
    sheet_count: int = None

    def __hash__(self):
        return hash(str(astuple(self)))

    def publish_xml(self, conns=None):
        xml_dict = {
            'tsRequest': {
                'workbook': {
                    '@name': self.name,
                    '@showTabs': str(self.show_tabs).lower(),
                    '@thumbnailsUserId': self.owner_id,
                    'project': {'@id': self.project_id}
                }
            }
        }
        if conns:
            xml_dict['tsRequest']['workbook'].setdefault('connections', list())
            for conn in conns:
                xml_dict['tsRequest']['workbook']['connections'].append({
                    'connection': {
                        '@serverAddress': conn['address'],
                        '@serverPort': conn['port'],
                        'connectionCredentials': {
                            '@name': conn['username'],
                            '@password': conn['password'],
                            '@embed': "true"
                        }
                    }
                })
        return xmltodict.unparse(xml_dict)


@dataclass
class Subscription(ServerObject):
    """ A Tableau Subscription object """
    content_id: str = None
    content_type: str = None
    schedule_id: str = None
    schedule_name: str = None
    user_id: str = None
    user_name: str = None
    subject: str = None
    message: str = None
    page_orientation: str = None
    page_size_option: str = None
    content_send_if_view_empty: bool = False
    attach_image: bool = False
    attach_pdf: bool = False
    suspended: bool = False

    def __hash__(self):
        return hash(str(astuple(self)))


@dataclass
class Schedule(ServerObject):
    """ A Tableau Schedule object """
    name: str = None
    state: str = None
    created_at: datetime = None
    updated_at: datetime = None
    next_run_at: datetime = None
    type: str = None
    frequency: str = None
    priority: int = None

    def __hash__(self):
        return hash(str(astuple(self)))


@dataclass
class Table(ServerObject):
    """ A Tableau Table object """
    name: str = None
    site_id: str = None
    schema: str = None
    tags: list = None
    is_embedded: bool = False
    is_certified: bool = False

    def __hash__(self):
        return hash(str(astuple(self)))


@dataclass
class Database(ServerObject):
    """ A Tableau Database object """
    name: str = None
    site_id: str = None
    connection_type: str = None
    type: str = None
    host_name: str = None
    content_permissions: str = None
    provider: str = None
    mime_type: str = None
    file_id: str = None
    request_url: str = None
    file_extension: str = None
    file_path: str = None
    tags: list = None
    is_embedded: bool = False
    is_certified: bool = False
    port: int = None

    def __hash__(self):
        return hash(str(astuple(self)))


@dataclass
class Job(ServerObject):
    created_at: datetime
    mode: str
    type: str
    updated_at: datetime = None
    completed_at: datetime = None
    finish_code: int = None
    extract_refresh_job_notes_datasource_id: str = None
    extract_refresh_job_notes_datasource_name: str = None
    extract_refresh_job_notes_workbook_id: str = None
    extract_refresh_job_notes_workbook_name: str = None

    def __hash__(self):
        return hash(str(astuple(self)))


if __name__ == '__main__':
    u1 = User(id='1', name='Bob', full_name='Bob Johnson')
    u2 = User(id='1', name='Bob')
    u3 = User(id='2', name='Tom')
    for u in {u1, u2, u3}:
        print(u.to_dict())
