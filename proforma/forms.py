from django import forms
from .models import *


#class ProformaReceiptForm(forms.Form):

 #   reference_Number        = forms.CharField()


class CreateProformaReceipt(forms.ModelForm):
    class Meta:
        model = ProformaReceipt
        fields = ['reference_Number', 'customer', 'date', 'sales_Officer',
                  'currency', 'discount_Rate', 'product', 'material_Color',
                  'unit_Price', 'quantity', 'charge_Vat'
                  ]
