import ipfsapi
import json
from filelock import FileLock
import base58

def file2bytes32(api, sample_file):
    content_hash = api.add(sample_file)
    bytes_array = base58.b58decode(hash_string) 
    return bytes_array[2:]
