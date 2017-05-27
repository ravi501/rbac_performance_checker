import unicodecsv
import os

def read_permissions_csv_file(num_permissions):
    permissions_list = []

    script_dir = os.path.dirname(__file__)
    full_path = os.path.join(script_dir, '../properties_files/permission-values.csv')
    with open(full_path, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        permissions_list = reader.fieldnames
    return permissions_list[:num_permissions]