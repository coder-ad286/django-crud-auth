from django.shortcuts import render
from django.http import JsonResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializers
from .models import Product
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@api_view(["GET"])
def apiOverview(req):
    api_urls={
        'List' : '/product-list/',
        'Detail View':'/product-detail/<int:id>',
        'Create' : '/product-create/',
        'Update' : '/product-update/<int:id>',
        'Delete' : '/product-delete/<int:id>'
    }
    
    return Response(api_urls)


class FetchProductsView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,req):
        print("called")
        products = Product.objects.all()
        serializers = ProductSerializers(products,many=True)
        return Response(serializers.data)

class FetchProductView(APIView):
    permission_classes =[IsAuthenticated]
    def get(self,req,id): 
        print(id)
        product = Product.objects.get(id=id)
        serializers = ProductSerializers(product,many=False)
        return Response(serializers.data)
    
class CreateProductView(APIView):
    permission_classes=[IsAuthenticated]
    @csrf_exempt
    def post(self,req):
        serializer = ProductSerializers(data=req.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        else:
            return JsonResponse({"success" : False,"message":"Invalid Product"},status=400)
        return Response(serializer.data)
    

class UpdateProductView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,req,id):
        product = Product.objects.filter(id=id).first()
        serializer = ProductSerializers(instance=product,data=req.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)  

class DeleteProductView(APIView):
    permission_classes=[IsAuthenticated]
    def delete(self,req,id):
        print("Id : ",id)
        product = Product.objects.filter(id=id).first()
        product.delete()
        return Response("Product Deleted Successfully...!")
    


    
    
    