"""
Created on Tue May  7 14:19:51 2024

@author: cmadaria
"""

# ? this package does not exist
from pybis_connection import connect

# ? is this module necessary


def get_properties_info(obj):
    for prop in obj.get_property_assignments():
        print(prop.code)


def check_instance():
    o = connect('serverA')
    info = []

    url = o.url

    instance = url.split('//')[1].split('.')[0]

    info.append(f'Checking contents in instance: {instance}\n')

    info.append(f'Listing SPACES in {instance}\n')
    info.append(f'Total number of SPACES: {str(o.get_spaces().totalCount)}\n')

    for space in o.get_spaces():
        info.append(f'  {space}')

    info.append(f'\nListing PROJECTS in {instance}\n')
    info.append(f'Total number of PROJECTS: {str(o.get_projects().totalCount)}\n')

    for project in o.get_projects():
        info.append(f'  {project.code}')

    info.append(f'\nListing EXPERIMENT TYPES in {instance}\n')
    info.append(
        f'Total number of EXPERIMENT TYPES: {str(o.get_experiment_types().totalCount)}\n'
    )

    for exp in o.get_experiment_types():
        info.append(f'  {exp}')

    info.append(f'\nListing OBJECT TYPES in {instance}\n')
    info.append(
        f'Total number of OBJECT TYPES: {str(o.get_object_types().totalCount)}\n'
    )

    objs = []
    for obj in o.get_object_types():
        objs.append(obj)
        info.append(f'  {obj}')

    for ob in objs:
        if ob.code == 'UNKNOWN':
            continue
        info.append(f'\nPROPERTY LIST for OBJECT {ob.code}\n')
        for prop in ob.get_property_assignments():
            info.append(f'{prop.code} --> {str(prop.dataType).lower()}')
        # print(ob.get_property_assignments())
        # i+=1
        # print(i)

    info.append(f'\nListing MATERIAL TYPES in {instance}\n')
    info.append(
        f'Total number of MATERIAL TYPES: {str(o.get_material_types().totalCount)}\n'
    )

    for material in o.get_material_types():
        info.append(f'  {material}')

    info.append(f'\nListing DATASET TYPES in {instance}\n')
    info.append(
        f'Total number of DATASET TYPES: {str(o.get_dataset_types().totalCount)}\n'
    )

    for dataset in o.get_dataset_types():
        info.append(f'  {dataset}')

    info.append(f'\nListing VOCABULARIES in {instance}\n')
    info.append(
        f'Total number of VOCABULARIES: {str(o.get_vocabularies().totalCount)}\n'
    )

    for vocab in o.get_vocabularies():
        info.append(f'  {vocab.code}')

    info.append(f'\nListing PLUGINS in {instance}\n')
    info.append(f'Total number of PLUGINS: {str(o.get_plugins().totalCount)}\n')

    for plug in o.get_plugins():
        info.append(f'  {plug.name}')

    return '\n'.join(info)
