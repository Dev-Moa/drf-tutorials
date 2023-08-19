import requests

endpoint = " http://127.0.0.1:8000/api/product/1"

get_Data = requests.get(endpoint)

print(get_Data.json())
