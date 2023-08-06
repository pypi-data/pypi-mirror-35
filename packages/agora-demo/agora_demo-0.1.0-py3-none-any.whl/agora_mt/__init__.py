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

def get_dataset(name):
    check_key_length(name)
    return json.loads(client.getter(name))
    #setter(name, str(value))
                


