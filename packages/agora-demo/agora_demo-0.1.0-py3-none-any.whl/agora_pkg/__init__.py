from client import *
from exceptions import *
import json
import pandas as pd

ds_prepend = 'ds_'
category_table = 'ct'
sch_prepend = 'sch_'
md_prepend = 'md_'

'''
Creating category table if it hasn't been created yet
'''

try:
    getter(category_table)
except Exception:
    ct = pd.DataFrame()
    ct['categ'] = []
    ct['dataset'] = []
    setter(category_table, str(ct.to_json()))



def get_dataset(dataset_name):
    try:
        ds = getter(ds_prepend + dataset_name)
    except:
        raise DatasetNotFoundError(dataset_name)
    return json.loads(ds)

def get_datasets():
    ct = pd.read_json(json.loads(getter(category_table)))
    return list(set(ct['dataset']))

def post_dataset(category, dataset_name, filepath):
    ct = pd.read_json(json.loads(getter(category_table)))
    ct.loc[len(ct)] = [category, dataset_name]
    dataset = pd.read_csv(filepath)
    dataset_exists = True
    try: 
        get_dataset(dataset)
    except: 
        dataset_exists = False
    if dataset_exists:
        raise DatasetExistsError(dataset)
    setter(category_table, ct)
    setter(ds_prepend + dataset_name, str(dataset.to_json()))
    setter(sch_prepend + dataset_name, str(pd.DataFrame(dataset.dtypes).to_json()))

def get_schema(dataset_name):
    try:
        sch = getter(ds_prepend + dataset_name)
    except:
        raise DatasetNotFoundError(dataset_name)
    return json.loads(sch)

def get_categories():
    ct = pd.read_json(json.loads(getter(category_table)))
    return list(set(ct['categ']))

def get_datasets_with_category(category):
    try:
        ds = list(ct[ct['categ'] == category]['dataset'])
    except KeyError:
        raise CategoryNotFoundError(category)


