import requests
print('hi')
from client import *
print('oh')
###TEST - doesn't work rn sadly
client = Client()
print('rip')
print(client.setter(123, "hi"))
print(client.getter(123))

# API_URL = 'http://agora5.jn6tkty4uh.us-west-1.elasticbeanstalk.com/'
# DATASET_NAME = 'blaap'
# FILEPATH = 'test.csv'
# METADATA = '672'
# header = {
#     'Content-Type': 'application/x-www-form-urlencoded',
# }

# params = {
#     'filepath': FILEPATH,
#     'dataset': DATASET_NAME,
#     'category': METADATA
# }

# response = requests.post(
#     API_URL + 'datasets',
#     headers=header,
#     data=params
# )
# print(response.text)
# response = requests.get(API_URL + 'datasets/' + DATASET_NAME)
# # print(pd.read_json(json.loads(response.text)))

# #response = requests.get('http://localhost:5000/datasets')
# print(response.text)