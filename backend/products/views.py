from django.http import Http404
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect
from rest_framework.views import APIView
# Create your views here.


class ProductDeleteView(APIView):
    def get(self,request,pk):
        product = get_object_or_404(Product,pk=pk)
        serializer = ProductSerializer(product,many=False).data
        return Response(serializer)
    def delete(self,request,pk):
        product = get_object_or_404(Product,pk=pk)
        product.delete()
        return Response(status=204)

class ProductUpdateView(APIView):
    def get(self,request,pk):
        product = get_object_or_404(Product,pk=pk)
        serializer = ProductSerializer(product,many=False).data
        return Response(serializer)

    def put(self, request, pk):
        product = get_object_or_404(Product,pk=pk)
        serializer = ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    
class ProductDetailView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product,pk=pk)
        serializer = ProductSerializer(product, many=False).data
        return Response(serializer)
       

class ProductAPIView(APIView):
    
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True).data
        return Response(serializer)
    
    def post(self,request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors,status=400)
