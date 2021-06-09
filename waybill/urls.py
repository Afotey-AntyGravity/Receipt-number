from django.urls import path

from .import views

app_name = 'waybill'
urlpatterns = [
    path('waybill/', views.waybillview, name='waybill_receipt'),

]
