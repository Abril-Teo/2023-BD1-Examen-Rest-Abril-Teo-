
from ..models import *
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q

class CustomerService():

    def getAllCustomers(self):
        return Customers.objects.all()

    def getCustomerById(self, pk):
        try:
            return Customers.objects.get(pk=pk)
        except Customers.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def deleteCustomer(self, pk):
        customer = self.getCustomerById(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def filtrarComienzaCon(self, letra):
        return Customers.objects.filter(contactname__startswith = letra)
    
    def updateCity(self, pk, newCity):
        customer = self.getCustomerById(pk)
        customer.city = newCity
        customer.save()

    def buscarPorNombreOContacto(self, termino):
        return Customers.objects.filter(Q(contactname__icontains=termino) | Q(contacttitle__icontains=termino))
    
    def obtenerPorNombre(self):
        return Customers.objects.order_by('contactname')

    
    


    
