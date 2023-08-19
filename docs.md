### lesson 1 : py client api 

> HTTP request will give back html response while REST_API HTTP Request will give back JSON response


```python

# To send request to endpoint use get method in requests library for example :

endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint)

# text property will print the body of response
print(get_response.text)


```

### Lesson 2: Run django project 

Basic setup for django project

### Lesson 3: Create your first API

Since REST_API response is json as mentioned earlier django comes with default JsonResponse function that helps to 
give json response to any request , basic example:

```python

def index(request):
    return JsonResponse({"message":"hi there"})
```
now this is just static data how about if we want dynamic data that comes from the user typings, Next Lesson.


### Lesson 3: Echo get Data 

the following will help as get data and addition info about request sent :

*request.headers*: Contains additional information or instructions about the request such as browser , authorization etc.
*request.body*: Carries the data sent in the request, such as form data or JSON.
*request.content_type*: Specifies the format or type of data in the request body.
*request.params*: Holds the parameters or data sent with the request, like api/q="this is params"?

to ech back , example :

```python
def index(request):
    body = request.body  # byte of string json
    request.GET
    data = {}
    try:
        data = json.loads(body)  # Loads function changes bit string JSON to python dictionary
        data['content_type'] = request.content_type
        data['headers'] = dict(request.headers)
        data['params'] = dict(request.GET)  # request.GET gets the urls of  GET request 

    except:
        pass
    return JsonResponse(data)
```
In the Next lesson we will learn how to make Models instance as Response

### Lesson 3: Django Model Instance as API Response

```python 

def index(request):
   # model instance
   products_data = Product.objects.all().order_by('?').first()
   # python dict 
   data = {}
   if products_data:
      data['id'] = products_data.id 
      data['title'] = products_data.title 
      data['description'] = products_data.description 
      data['price'] = products_data.price 
    # JSON
   return JsonResponse(data)


# model instance -> python dict -> return JSONResponse to client
```

We can simplify this process and the Next lesson we are Learning : django model instance to python dict

### Lesson 4: Django Model Instance to Python Dictionary

```python 

from django.forms.models import model_to_dict
def index(request):
   products_data = Product.objects.all().order_by('?').first()
   data = {}
   if products_data:
      data = model_to_dict(products_data,fields=['id'])
   return JsonResponse(data)
```

- model_to_dict method changes models instance to dictionary and process is simpler than before.
- Up to now we are using django to give JSONResponse to api requests now in the next lesson we will start django rest framework


### Lesson 4: Django Rest Framework Response

```python 

from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response 
from rest_framework.decorators import api_view

# Create your views here.

@api_view(["GET"])
def index(request):
   products_data = Product.objects.all().order_by('?').first()
   data = {}
   if products_data:
      data = model_to_dict(products_data,)
   return Response(data)

```
in drf we can use something called serializer that will help convert our models to JSON response
and also will alot under the hood in the next lesson we look into it .


### Lesson 4: Django Rest Framework : Serializers

Serializers are kind similiar to forms they make process of geting and sending data through api easy .

```python

## products/serializer.py

from rest_framework.serializers import ModelSerializer #similiar to ModelForms directly relates to models and get or post the models
from .models import Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


## api/views.py
# N.B dont create models inside api app 

from products.models import Product 
from rest_framework.response import Response
from rest_framework.decorators import api_view  # api view tells what type of api request a view will accept
from products.serializers import ProductSerializer 
# Create your views here.

@api_view(["GET"])
def index(request):
   instance = Product.objects.all().order_by('?').first()
   data = {}
   if instance:
      data = ProductSerializer(instance=instance).data
   return Response(data)

```
since now we are getting data from our app using api's GET now we want to ingets or post data , in the next lesson we will explore it .


### Lesson 4: Django Rest Framework : ingest data / post data 


client

```python
import requests

endpoint = " http://127.0.0.1:8000/api/"

post_Data = requests.post(endpoint,json={'title':'hello world','description':"test", 'price':199})

print(post_Data)

```

server

```python 
@api_view(["POST"])
def index(request):
    data=request.data  # get the data to save NOT request.post as we done it in django
    serializer = ProductSerializer() # serialize it
    if serializer.is_valid(raise_exception=True): # validate the data and also raise exception if not valid
        serializer.save()  # if valid save it to the DB
        return Response(serializer.data) 
    return Response('{"error":"not good data"}')

```


________________________________ CRUD IN REST API  _________________________________________________________________
## CREATE_API 

``` python

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

```
## LIST_CREATE_API = list and create both 

```python

class ProductCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(["GET","POST"])
def productListView(request):
    if request.method == "GET":
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)


@api_view(["GET","POST"])
def productCreateView(request):
    if request.method == "GET":
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    
    if request.method == 'POST':
        posted_data = request.data
        serializer = ProductSerializer(data=posted_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status=400)
        

```

## RETRIEVE_API  = DETAIL VIEW

```python

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# function based
@api_view(["GET","POST"]) 
def productDetailView(request,pk):
    if request.method == "GET":
        if pk is not None :
            obj = get_object_or_404(Product,pk=pk)
            data = ProductSerializer(obj,many=False).data
            return Response(data)

```


Now lets learn How to do Update and destroy AKA Delete 

### Update API and Destroy API

