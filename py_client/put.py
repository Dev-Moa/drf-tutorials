
import requests


endpoint = "http://127.0.0.1:8000/api/product/10/update/"
data = {
    "title":"updated",
    "description":"update put"
}



update = requests.put(endpoint,json=data)