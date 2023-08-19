import requests

endpoint = " http://127.0.0.1:8000/api/product/"

data = {'title':'created one','description':"last one", 'price':1}
# POST
post_Data = requests.post(endpoint,json=data)

print(post_Data.status_code)
