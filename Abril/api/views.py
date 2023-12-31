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
    
# =====================================   CATEGORIES   =================================== # 
@api_view(["GET", "POST"])
def categories(request):
    if request.method == "GET":         
        categories = Categories.objects.all()
        categoriesSerializers = CategorieSerializer(categories, many=True)
        return Response(categoriesSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        categorieNuevo = CategorieSerializer(data = request.data)
        if categorieNuevo.is_valid():
            categorieNuevo.save()
            return Response(categorieNuevo.data, status=status.HTTP_200_OK)
        return Response(categorieNuevo.errors ,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET", "PUT", "DELETE"])
def id_categories(request, pk):
    try:
        categorie = Categories.objects.get(categoryid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = CategorieSerializer(categorie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        request.data['categoryid'] = pk
    
        serializer = CategorieSerializer(categorie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        categorie.delete()
        return Response(status=status.HTTP_200_OK)

# =====================================   PRODUCTS   =================================== #
@api_view(["GET", "POST"])
def products(request):
    if request.method == "GET":         
        products = Products.objects.all()
        productSerializers = ProductSerializer(products, many=True)
        return Response(productSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        productNuevo = ProductSerializer(data=request.data)
        if productNuevo.is_valid():
            productNuevo.save()
            return Response(productNuevo.data, status=status.HTTP_200_OK)
        return Response(productNuevo.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def id_products(request, pk):
    try:
        product = Products.objects.get(productid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        request.data['productid'] = pk
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_200_OK)

# =====================================   ORDERS   =================================== #

@api_view(["GET", "POST"])
def orders(request):
    if request.method == "GET":         
        orders = Orders.objects.all()
        orderSerializers = OrderSerializer(orders, many=True)
        return Response(orderSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        orderNuevo = OrderSerializer(data=request.data)
        if orderNuevo.is_valid():
            orderNuevo.save()
            return Response(orderNuevo.data, status=status.HTTP_200_OK)
        return Response(orderNuevo.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def id_orders(request, pk):
    try:
        order = Orders.objects.get(orderid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        request.data['orderid'] = pk
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_200_OK)

# =====================================   ORDER_DETAILS   =================================== #

@api_view(["GET", "POST"])
def order_details(request):
    if request.method == "GET":         
        order_details = Orderdetails.objects.all()
        orderDetailsSerializers = OrderdetailSerializer(order_details, many=True)
        return Response(orderDetailsSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        orderDetailNuevo = OrderdetailSerializer(data=request.data)
        if orderDetailNuevo.is_valid():
            orderDetailNuevo.save()
            return Response(orderDetailNuevo.data, status=status.HTTP_200_OK)
        return Response(orderDetailNuevo.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def id_order_details(request, pk, pk2):
    try:
        order_detail = Orderdetails.objects.get(orderid=pk, productid=pk2)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        serializer = OrderdetailSerializer(order_detail)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        request.data['orderid'] = pk
        serializer = OrderdetailSerializer(order_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        order_detail.delete()
        return Response(status=status.HTTP_200_OK)

# =====================================   EMPLOYES   =================================== #

@api_view(["GET", "POST"])
def employees(request):
    if request.method == "GET":         
        employees = Employees.objects.all()
        employeeSerializers = EmployeeSerializer(employees, many=True)
        return Response(employeeSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        employeeNuevo = EmployeeSerializer(data=request.data)
        if employeeNuevo.is_valid():
            employeeNuevo.save()
            return Response(employeeNuevo.data, status=status.HTTP_200_OK)
        return Response(employeeNuevo.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def id_employees(request, pk):
    try:
        employee = Employees.objects.get(employeeid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        request.data['employee_id'] = pk
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_200_OK)
    
    
    #mostrar todos los productos, (id del producto,nombre del producto,nombre de la categoria) cuyo nombre comienze con la letra C y nombre de la categoria sea = Beverages

@api_view(["GET"])
def filtro2(request):
    products = Products.objects.filter(productname__startswith= 'C', categoryid__categoryname = "Beverages")
    productSerializers = ProductSerializer(products, many=True)
    return Response(productSerializers.data, status=status.HTTP_200_OK)
#filtrar por fecha de birthday antes del 15 de noviembre de 2005
from datetime import datetime

@api_view(["GET"])
def filtro1(request):
    # Filter employees by birthday before November 15, 2005
    employees = Employees.objects.filter(birthday__lt=datetime(1948, 12, 8, 00, 00, 00, 00))
    employeeSerializers = EmployeeSerializer(employees, many=True)
    return Response(employeeSerializers.data, status=status.HTTP_200_OK)

    #employees cuyo country contenga una vocal y cuyo salary sea mayor a 3000 y cuyo birthday sea antes del 1 de enero de 1990 teniendo en cuenta que la estructura que usa para el birthday es un datetime asi: "birthdate": "1937-09-19T00:00:00Z"
from datetime import datetime
from django.db.models import Q

@api_view(["GET", 'UPDATE'])
def filtro3(request):

    employees = Employees.objects.filter(Q(country__icontains='a') | Q(country__icontains='e') | Q(country__icontains='i') | Q(country__icontains='o') | Q(country__icontains='u'), salary__gt=2800, birthdate__lt=datetime(1990, 1, 1))

    employees.update(salary=5555)

    employeeSerializers = EmployeeSerializer(employees, many=True)
    return Response(employeeSerializers.data, status=status.HTTP_200_OK)

'''
@api_view(["GET", 'UPDATE'])
def filtro4(request):
    letra = request.query_params.get("letter")
    year = request.query_params.get("year")

    empleadosFiltrados = Employees.objects.filter(firstname__icontains = letra)
    resultados = []
    for e in empleadosFiltrados:
        resultado = {
            "id" : e.employeeid,
            "nombre" : e.firstname,
            "apellido" : e.lastname,
            "birthdate" : e.birthdate,
            "country" : e.country,
            "newCountry" : request.query_params.get("newCountry"),
        }
        if e.birthdate.year >= int(year):
            resultados.append(resultado)
            e.country = request.query_params.get("newCountry")
            e.save()

    serializados = Filtro4Serializer(resultados, many=True)
    return Response(serializados.data)
'''

@api_view(["GET"])
def punto2(request):
    letra = request.query_params.get("letter")
    year = request.query_params.get("year")

    empleadosFiltrados = Employees.objects.filter(firstname__icontains = letra, birthdate__year__gte = year)
    resultados = []
    for e in empleadosFiltrados:
        resultado = {
            "id" : e.employeeid,
            "nombre" : e.firstname,
            "apellido" : e.lastname,
            "birthdate" : e.birthdate,
            "country" : e.country,
            "newCountry" : request.query_params.get("newCountry"),
        }
        resultados.append(resultado)
        e.country = request.query_params.get("newCountry")
        e.save()

    serializados = Filtro4Serializer(resultados, many=True)
    return Response(serializados.data)


@api_view(['GET'])
def punto1(request):
    categoria = request.query_params.get("categoryid")
    ventas = request.query_params.get("ventasmin")

    detalle_ordenes = Orderdetails.objects.filter(productid__categoryid = categoria) 
    resultados = []
    for e in detalle_ordenes:
        precioTotal = 0
        precioTotal += e.subTotal()
        ordenes = e.orderid
        #print("aaaaaaa" , ordenes.employeeid.nomCompleto())


        empleado = ordenes.employeeid
        print(empleado)
        resultado = {
            "EmployeeID" : empleado.getId(),
            "NombreCompleto_del_empleado" : empleado.nomCompleto(),
            "Ganancias_Totales" : precioTotal,
            "Hire_Date" : empleado.getHireDate,
        }
        if precioTotal >= int(ventas):
                    resultados.append(resultado)
    
    '''
    empleadoActual = O
    for i in resultados:
        for y in resultados:
            if y.EmployeedID == empleadoActual:
                Ganancias_Totales += Ganancias_Totales
    '''
    serializados = Punto1Serializer(resultados, many=True)
    return Response(serializados.data)