from .client import *
from .exceptions import *
import json
import pandas as pd
import os

ds_prepend = 'ds_'
category_table = 'ct'
sch_prepend = 'sch_'
md_prepend = 'md_'

client = Client()
'''
Creating category table if it hasn't been created yet

name = "example_pkg"

try:
    client.getter(category_table)
except Exception:
    ct = pd.DataFrame()
    ct['categ'] = []
    ct['dataset'] = []
    client.setter(category_table, str(ct.to_json()))
'''
def check_key_length(key):
    if len(key) > 30:
        raise InvalidKeyError(key)

def post_dataset(filepath, name):
    check_key_length(name)
    value = {}
    folders = filter(os.path.isdir, os.listdir(filepath))
    for folder in folders:
        folder_dict = {}
        folder_path = filepath + "/" + folder
        files = os.listdir(folder_path)
        for file in files:
            if file[:2] == 'md':
                metadata = pd.read_csv(folder_path + "/" + file)
                folder_dict['md'] = metadata.to_json()
            elif file[:2] == 'ds':
                dataset = pd.read_csv(folder_path + "/" + file)
                sample = dataset.sample(frac=0.1)
                folder_dict['ds'] = sample.to_json()
        value[folder] = folder_dict
    print(value)
    #setter(name, str(value))
                


