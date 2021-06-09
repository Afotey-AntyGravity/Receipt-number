from django.urls import path

from .import views

app_name = 'proforma'
urlpatterns = [
    path('proformareceipt/', views.proformaview, name='proforma_receipt'),
    path('proformastandard/', views.proformastandard, name='proforma_standard'),
    path('create_proformastandard/', views.createproformastandard, name='create_proforma_standard'),
]
