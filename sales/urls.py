from django.urls import path

from .import views

app_name = 'sales'
urlpatterns = [
    path('salesreceipt/', views.referenceview, name='sales_receipt'),

]
