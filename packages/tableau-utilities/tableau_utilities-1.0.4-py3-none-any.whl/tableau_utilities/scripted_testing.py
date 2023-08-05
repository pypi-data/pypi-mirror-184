import os
import yaml
import shutil
import xml.etree.ElementTree as ET
from pprint import pprint, isreadable
from tableau_utilities import Datasource, TableauServer
from tableau_utilities import tableau_file_objects as tfo


if __name__ == '__main__':
    with open('settings.yaml') as f:
        settings = yaml.safe_load(f)
    tmp_folder = 'tmp_downloads'
    # Cleanup lingering files, if there are any
    # shutil.rmtree(tmp_folder, ignore_errors=True)

    # Create a temp directory for testing
    os.makedirs(tmp_folder, exist_ok=True)
    os.chdir(tmp_folder)

    #  ### ### Testing here ### ###

    # Connect to Tableau Server
    ts = TableauServer(**settings['tableau_login'])
    datasources = [d for d in ts.get_datasources()]
    # print(datasources)
    # Loop through the datasources
    # for d in datasources:
    # for path in os.listdir():
    #     if path != 'Jobs.tdsx':
    #         continue
        # path = ts.download_datasource(datasource_id=d.id)
        # datasource = Datasource(path)
        # datasource._tree.write(path.replace('.tdsx',  '.tds'))
        # datasource.save()
        # column = tfo.Column(
        #     name='FRIENDLY_NAME',
        #     caption='Friendly Name',
        #     datatype='string',
        #     type='ordinal',
        #     role='dimension',
        #     desc='Nice and friendly',
        # )
        # datasource.enforce_column(column, remote_name='ORG_ID', folder_name='Org')
        # print(datasource.folders.get('Org'))
        # print(datasource.datasource_metadata.get('ORG_ID'))
        # print(datasource.extract_metadata.get('ORG_ID'))
        # print(datasource.datasource_mapping_cols.get(column.name))
        # print(datasource.extract_mapping_cols.get(column.name))

    # ### ### ### ### ### ### ###

    # Cleanup lingering files, if there are any
    # os.chdir('..')
    # shutil.rmtree(tmp_folder)
