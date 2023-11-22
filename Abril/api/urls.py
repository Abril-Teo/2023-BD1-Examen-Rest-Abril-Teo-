from django.urls import path, include
from .views import *

urlpatterns = [
    path("customer/", customers, name="getAllCustomers"),
    path("customer/<str:pk>", id_customers , name="getCustomerById"),

    path("supplier/", suppliers, name="getAllSuppliers"),
    path("supplier/<str:pk>", id_suppliers , name="getSupplierById"),

]