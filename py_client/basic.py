import requests

endpoint = " http://127.0.0.1:8000/api/product/"

data = {'title':'working one','description':"last one", 'price':1}
# POST
post_Data = requests.post(endpoint,json=data)
# GET 
get_Data = requests.get(endpoint)

print(post_Data.text)
