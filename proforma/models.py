#from django.db import models
from django.utils import timezone
from tools.models import *

# Create your models here.

import random
import datetime



#----------------Proforma Invoices------------------------------->
#----------------Proforma Receipt(Standard)------------------>
class ProformaReceipt(models.Model):



    reference_Number = models.CharField(max_length=200, null=True)
    customer = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(default=timezone.now)
    sales_Officer = models.ForeignKey(SalesManInformation, null=True, on_delete= models.SET_NULL)
    currency = models.ForeignKey(Currency, null=True, on_delete= models.SET_NULL)
    discount_Rate = models.FloatField(null=True)
    #-----Second lock-------->
    product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
    material_Color = models.ForeignKey(MaterialColourInformation, null=True, on_delete= models.SET_NULL)
    unit_Price = models.FloatField(null=True)
    quantity = models.PositiveIntegerField(default=0)
    charge_Vat = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    #invoice Total
    #VAT %
    #total discount
    #total Payment
    #net balance

    def __str__(self):
        return self.reference_Number

#----------------Proforma Receipt(Long Span)------------------>
class LongSpanReceipt(models.Model):
    MODE = (
        ('Actual Invoice', 'Actual Invoice'),
        ('Provisional Invoice', 'Provisional Invoice'),
    )

    reference_Number = models.CharField(max_length=200, null=True)
    #Existing Customer
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    #discount Rate
    location = models.CharField(max_length=200, null=True)
    currency = models.ForeignKey(Currency, null=True, on_delete= models.SET_NULL)
    #color
    #site location area
    #branch id
    #telephone
    #contact person
    #address
    #profile
    #gauge

