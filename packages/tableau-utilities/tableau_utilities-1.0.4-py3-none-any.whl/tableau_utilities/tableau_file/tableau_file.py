import xml.etree.ElementTree as ET
import os
import re

import yaml
import xmltodict
import shutil
from copy import deepcopy
from zipfile import ZipFile

from tableau_utilities.tableau_file.tableau_file_objects \
    import FileObject, Column, Connection, Folder, FolderItem, MetadataRecord, MappingCol, Relation
from tableau_utilities.general.funcs import convert_to_snake_case


with open(os.path.join(os.path.dirname(__file__), 'item_types.yml')) as f:
    CONFIG = yaml.safe_load(f)

ITEM_CLASS = {
    'column': Column,
    'connection': Connection,
    'relation': Relation,
    'folder': Folder,
    'datasource_metadata': MetadataRecord,
    'extract_metadata': MetadataRecord,
    'datasource_mapping_cols': MappingCol,
    'extract_mapping_cols': MappingCol,
}


class TableauFileError(Exception):
    """ A minimum viable exception. """

    def __init__(self, message):
        self.message = message


def transform_tableau_item(item):
    """ Transform a Tableau item.

    Args:
        item (dict): The dict Tableau item
    """
    # Transform the item dict
    update = dict()
    prep = dict()
    prep.update(item)
    folder_items = item.get('folder-item')
    if 'connection' in prep:
        prep.update(prep['connection'])
        del prep['connection']
    if 'collation' in prep:
        for k, v in prep['collation'].items():
            prep[f'collation_{k}'] = v
        del prep['collation']
    if folder_items:
        prep['folder-item'] = list()
        if isinstance(folder_items, list):
            for folder_item in folder_items:
                folder_item = {k.replace('@', ''): v for k, v in folder_item.items()}
                prep['folder-item'].append(FolderItem(**folder_item))
        elif isinstance(folder_items, dict):
            folder_item = {k.replace('@', ''): v for k, v in folder_items.items()}
            prep['folder-item'].append(FolderItem(**folder_item))
        else:
            raise TableauFileError(f'Cannot transform folder-item. Unexpected type: {type(folder_items)}')
    for key, value in prep.items():
        # Update item keys "@someThing-like...this" to "this"
        key = re.sub(r'.+\.\.\.', '', key)
        key = key.replace('ns0_', '').replace('_ns0', '')
        key = convert_to_snake_case(key)
        if key == 'class':
            update['class_name'] = value
        else:
            update[key] = deepcopy(value)
    return update


class DatasourceItems:
    """
        A list of FileObject items from a Tableau Datasource,
        i.e. Columns, Folders, Connections, etc
    """
    def __init__(self, seq=(), item_name='column'):
        # Set and validate
        if item_name in ITEM_CLASS:
            self._item_name = item_name
            self._item = ITEM_CLASS[item_name]
            self._tag = CONFIG[item_name]['tag']
            self._paths = CONFIG[item_name]['xpath']
        else:
            raise TableauFileError(f'Invalid item - must be one of: {ITEM_CLASS.keys()}')
        # Enforce listed items
        for idx, item in enumerate(seq):
            seq[idx] = self.__validate_item(item)
        self.__items = list(seq)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.__items[item]
        return self.__items[self.__items.index(item)]

    def __setitem__(self, item, newitem):
        if isinstance(item, int):
            self.__items[item] = newitem
        else:
            self.__items[self.__items.index(item)] = newitem

    def __iter__(self):
        for item in self.__items:
            yield item

    def __len__(self):
        return len(self.__items)

    def __eq__(self, other):
        same = True
        for item in self.__items:
            if item not in other:
                same = False
        for item in other:
            if item not in self.__items:
                same = False
        return same

    def __str__(self):
        return f'{self.__class__.__name__}({self.__items})'

    def __repr__(self):
        return self.__str__()

    def __del__(self):
        self.__items.clear()

    def __validate_item(self, item):
        if isinstance(item, dict):
            _item = transform_tableau_item(item)
            try:
                return self._item(**_item)
            except TypeError as err:
                print(item)
                print(_item)
                raise TableauFileError(err) from err
        elif not isinstance(item, self._item):
            raise TableauFileError(f'Item must be of type {self._item} or {dict}')
        return item

    def _to_dict(self):
        """ Converts all items into dicts """
        for idx, item in enumerate(self.__items):
            if isinstance(item, type(self._item)):
                self.__items[idx] = item.dict()

    def _to_obj(self):
        """ Converts all items into the appropriate Tableau FileObject """
        for idx, item in enumerate(self.__items):
            if isinstance(item, dict):
                item = transform_tableau_item(item)
                self.__items[idx] = self._item(**item)

    def add(self, item):
        """ Add the provided item to the list

        Args:
            item (dict|FileObject): The item to be added
        """
        item = self.__validate_item(item)
        if item in self.__items:
            raise TableauFileError(f'Item already exists: {item}')
        self.__items.append(item)

    def update(self, item):
        """ Add the provided item to the list

        Args:
            item (dict|FileObject): The item to be added
        """
        item = self.__validate_item(item)
        self[item] = item

    def get(self, item):
        """ Get the item from the list

        Args:
            item (dict|str|FileObject): The item to get

        Returns: The Tableau FileObject
        """
        if isinstance(item, int):
            return self.__items[item]
        for _item in self.__items:
            if _item == item:
                return _item

    def delete(self, item):
        """ Delete the item from the list

        Args:
            item (dict|str|FileObject): The item to delete
        """
        self.__items.remove(item)

    def pop(self, item):
        """ Delete and return the item from the list

        Args:
            item (dict|str|FileObject): The item to delete

        Returns: The Tableau FileObject
        """
        return self.__items.pop(self.__items.index(item))


class TableauFile:
    """ The base class for a Tableau file, i.e. Datasource or Workbook. """

    def __init__(self, file_path):
        """
        Args:
            file_path (str): Path to a Tableau file
        """
        self.file_path = os.path.abspath(file_path)
        self.extension = file_path.split('.')[-1]
        ''' Set on init '''
        self._tree: ET.ElementTree
        self._root: ET.Element
        self.__extract_xml()

    def unzip(self, path=None, unzip_all=False):
        """ Unzips the Tableau File.

        Args:
            path (str): The path to the zipped Tableau file
            unzip_all (bool): True to unzip all zipped files

        Returns: The path to the unzipped Tableau File
        """
        if not path:
            path = self.file_path
        file_dir = os.path.dirname(path)
        tableau_file_path = None
        with ZipFile(path) as zip_file:
            for z in zip_file.filelist:
                ext = z.filename.split('.')[-1]
                if unzip_all:
                    zip_file.extract(member=z, path=file_dir)
                    if ext in ['tds', 'twb']:
                        tableau_file_path = os.path.join(file_dir, z.filename)
                elif not unzip_all and ext in ['tds', 'twb']:
                    zip_file.extract(member=z, path=file_dir)
                    tableau_file_path = os.path.join(file_dir, z.filename)
        return tableau_file_path

    def __extract_xml(self):
        """ Extracts the XML from a Tableau file """
        if self.extension in ['tdsx', 'twbx']:
            path = self.unzip()
        else:
            path = self.file_path

        self._tree = ET.parse(path)
        self._root = self._tree.getroot()

        if self.extension in ['tdsx', 'twbx']:
            os.remove(path)

    def save(self):
        """ Save/Update the Tableau file with the XML changes made """
        if self.extension in ['tdsx', 'twbx']:
            file_name = os.path.basename(self.file_path)
            file_folder = os.path.dirname(self.file_path)
            # Move zipped Tableau file into a temporary folder while updating
            temp_folder = os.path.join(file_folder, 'TMP ' + '.'.join(file_name.split('.')[:-1]).strip())
            os.makedirs(temp_folder, exist_ok=True)
            temp_file_path = os.path.join(temp_folder, file_name)
            shutil.move(self.file_path, temp_file_path)
            # Unzip the files from the Tableau file
            tableau_file_path = self.unzip(temp_file_path, unzip_all=True)
            # Update the Tableau file's contents
            self._tree.write(tableau_file_path)
            # Repack the file
            with ZipFile(temp_file_path, 'w') as z:
                for file in os.listdir(temp_folder):
                    if file == file_name:  # Skip the zipped file
                        continue
                    z.write(os.path.join(temp_folder, file), arcname=file)
            # Move zipped Tableau file back to the original folder and remove any unpacked content
            shutil.move(temp_file_path, self.file_path)
            shutil.rmtree(temp_folder)
        else:
            # Update the Tableau file's contents
            self._tree.write(self.file_path)


class Datasource(TableauFile):
    """
        A class representation of a Tableau Datasource.
        Used to update a Tableau Datasource by interacting with various elements,
        such as Columns, Folders, Connections, Metadata, etc.
    """

    def __init__(self, file_path):
        """
        Args:
            file_path (str): Path to a Tableau Datasource file; tds or tdsx
        """
        super().__init__(file_path)
        # Validate the file on initialization
        if self.extension not in ['tds', 'tdsx']:
            raise TableauFileError('File must be TDS or TDSX')

        self.columns: DatasourceItems[Column] = DatasourceItems(item_name='column')
        self.connections: DatasourceItems[Connection] = DatasourceItems(item_name='connection')
        self.relations: DatasourceItems[Relation] = DatasourceItems(item_name='relation')
        self.folders: DatasourceItems[Folder] = DatasourceItems(item_name='folder')
        self.datasource_metadata: DatasourceItems[MetadataRecord] = DatasourceItems(item_name='datasource_metadata')
        self.extract_metadata: DatasourceItems[MetadataRecord] = DatasourceItems(item_name='extract_metadata')
        self.datasource_mapping_cols: DatasourceItems[MappingCol] = DatasourceItems(item_name='datasource_mapping_cols')
        self.extract_mapping_cols: DatasourceItems[MappingCol] = DatasourceItems(item_name='extract_mapping_cols')
        self.__set_sections()

    def sections(self):
        """ Yields each section defined in the class, for iteration """
        yield self.columns
        yield self.connections
        yield self.relations
        yield self.folders
        yield self.datasource_metadata
        yield self.extract_metadata
        yield self.datasource_mapping_cols
        yield self.extract_mapping_cols

    @staticmethod
    def __confirm_tag(element, tag):
        """ Confirms the tag, based on tags of sub elements of the element.

        Args:
            element (ET.Element):
            tag (str):

        Returns: The correct tag
        """
        # Gets the element tag
        tags = list({e.tag for e in element})
        if tag not in tags:
            tags = [t for t in tags if t.endswith(f'true...{tag}')]
            return tags[0] if tags else tag
        return tag

    def __get_section_parent(self, xpaths):
        """ Gets the parent element for the section

        Args:
             xpaths (list): A list of xpaths that lead to the section
        """
        # Loop through the xpaths until the section has been identified
        for xpath in xpaths:
            parent = self._root.find(xpath)
            if parent:
                return parent
        return None

    def __set_sections(self):
        """ Sets DatasourceItems for each section """
        for section in self.sections():
            parent = self.__get_section_parent(section._paths)
            if not parent:
                continue
            tag = self.__confirm_tag(parent, section._tag)
            # Gets elements within the parent element, with the appropriate section.tag,
            # and adds them to the section items
            for element in parent.iter(tag):
                item = xmltodict.parse(ET.tostring(element))[tag]
                section.add(item)

    def enforce_column(self, column: Column, folder_name=None, remote_name=None):
        """
            Enforces a column by:
                - Adding the column if it doesn't exist, otherwise updating it to match the column
                - Adding the column's corresponding folder-item to the appropriate folder, if it doesn't exist
                    - Create the folder if it doesn't exist
                - Updating the metadata local-name to map to the column name
                - Adding the column mapping to the mapping cols, if it doesn't exist

        Args:
            column (Column): The TableFile Column object
            remote_name (str): The name of the column from the connection (not required for Tableau Calculations),
             i.e. the SQL alias if the connection is a SQL query
            folder_name (str): The name of the folder that the column should be in

        """
        # Add Column
        if column not in self.columns:
            self.columns.add(column)
        # Update the Column
        else:
            self.columns.update(column)
        # Add Folder / FolderItem for the column, if folder_name was provided
        if folder_name:
            folder = self.folders.get(folder_name)
            folder_item = FolderItem(name=column.name)
            if folder and folder_item not in folder.folder_item:
                folder.folder_item.append(folder_item)
                self.folders.update(folder)
            elif not folder:
                self.folders.add(Folder(name=folder_name, folder_item=[folder_item]))
        # If a remote_name was provided, and the column is not a Tableau Calculation - enforce metadata
        if remote_name and not column.calculation:
            # Update MetadataRecords
            datasource_record = self.datasource_metadata.get(remote_name)
            datasource_record.local_name = column.name
            self.datasource_metadata.update(datasource_record)
            extract_record = self.extract_metadata.get(remote_name)
            extract_record.local_name = column.name
            self.extract_metadata.update(extract_record)
            # Update MappingCols
            if not self.datasource_mapping_cols.get(column.name):
                self.datasource_mapping_cols.add(
                    MappingCol(key=column.name, value=f'{datasource_record.parent_name}.[{remote_name}]')
                )
            if not self.extract_mapping_cols.get(column.name):
                self.extract_mapping_cols.add(
                    MappingCol(key=column.name, value=f'{extract_record.parent_name}.[{remote_name}]')
                )

    def save(self):
        """ Save all changes made to each section of the Datasource """
        for section in self.sections():
            parent = self.__get_section_parent(section._paths)
            if not parent:
                continue
            tag = self.__confirm_tag(parent, section._tag)
            # Find all elements within the parent element, and the index of those elements
            elements = [(idx, element) for idx, element in enumerate(parent) if element.tag == tag]
            # Index of the first element identified
            starting_index = elements[0][0] if elements else -1
            # Remove the existing items
            for _, e in elements:
                parent.remove(e)
            # Insert the new / updated items
            for item in section:
                parent.insert(
                    starting_index,
                    ET.fromstring(xmltodict.unparse({tag: item.dict()}, pretty=True))
                )
        super().save()


if __name__ == '__main__':
    # Params
    ds_path = 'downloads/Users + Orgs.tdsx'

    unzip = False
    unzip_all_files = False

    ds = Datasource(ds_path)
    if unzip:
        ds.unzip(unzip_all=unzip_all_files)

    print(ds.columns.get('[USER_ID]'))
