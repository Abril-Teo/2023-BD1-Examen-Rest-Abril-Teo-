from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Customers, Suppliers, Categories, Products, Orders, Orderdetails, Employees

class SerializadorPadre(ModelSerializer):
    class Meta:
        fields = '__all__'

class CustomerSerializer(SerializadorPadre):
    class Meta:
        model = Customers
        fields = '__all__'

class SupplierSerializer(SerializadorPadre):
    class Meta:
        model = Suppliers
        fields = '__all__'

class CategorieSerializer (SerializadorPadre):
   class Meta:
      model = Categories
      fields = '__all__'

class ProductSerializer (SerializadorPadre):
   #categoryid = CategorieSerializer(many=False, required=False)
   class Meta:
      model = Products
      fields = '__all__'

class OrderdetailSerializer (SerializadorPadre):
   class Meta:
      model = Orderdetails
      fields = '__all__'

class OrderSerializer(SerializadorPadre):
   order_details = OrderdetailSerializer(many=True, read_only=True)

   class Meta:
      model = Orders
      fields = '__all__'

class EmployeeSerializer (SerializadorPadre):
   class Meta:
      model = Employees
      fields = '__all__'

class Filtro4Serializer(serializers.Serializer):
   id = serializers.IntegerField()
   apellido = serializers.CharField()
   nombre = serializers.CharField()
   birthdate = serializers.DateTimeField()
   country = serializers.CharField()
   newCountry = serializers.CharField()


class Punto1Serializer(serializers.Serializer):
   EmployeeID = serializers.CharField()
   NombreCompleto_del_empleado = serializers.CharField()
   Ganancias_Totales = serializers.CharField()
   Hire_Date = serializers.CharField()
