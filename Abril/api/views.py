from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import *
from api.serializers import * 

# =====================================   COSTUMERS   =================================== #
@api_view(['GET', 'POST'])
def customers(request):
    if request.method == 'GET':
        customers = Customers.objects.all()
        #customers = Customers.objects.filter(contactname__startswith = 'T')[:4]
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def id_customers(request, pk):
    try :
        customers = Customers.objects.get(pk=pk)
    except Customers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CustomerSerializer(customers)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomerSerializer(customers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        customers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# =====================================   SUPPLIERS   =================================== #

@api_view(['GET', 'POST'])
def suppliers(request):
    if request.method == 'GET':
        suppliers = Suppliers.objects.all()
        serializer = SupplierSerializer(suppliers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def id_suppliers(request, pk):
    try :
        suppliers = Suppliers.objects.get(pk=pk)
    except Suppliers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SupplierSerializer(suppliers)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SupplierSerializer(suppliers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        suppliers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)