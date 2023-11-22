from django.urls import path, include
from .views import *

urlpatterns = [
    path("customer/", customers, name="getAllCustomers"),
    path("customer/<str:pk>", id_customers , name="getCustomerById"),

    path("supplier/", suppliers, name="getAllSuppliers"),
    path("supplier/<str:pk>", id_suppliers , name="getSupplierById"),

    path("category/", categories, name="getAllCategories"),
    path("category/<int:pk>", id_categories , name="getCategoryById"), 

    path("product/", products, name="getAllProducts"),
    path("product/<str:pk>", id_products , name="getProductById"), 

    path("order/", orders, name="getAllOrders"),
    path("order/<str:pk>/", id_orders, name="getOrderById"),

    path("orderdetail/", order_details, name="getAllOrderDetails"),
    path("orderdetail/<str:pk>/<str:pk2>", id_order_details, name="getOrderDetailById"),

    path("employee/", employees, name="getAllEmployees"),
    path("employee/<str:pk>/", id_employees, name="getEmployeeById"),

    path("filtro1/", filtro1, name="filtro1")
]