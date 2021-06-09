from django import forms
from .models import *


class CreateCustomer(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','phone','email','address']

  #  widgets ={
   # 'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name...'}),
    #'phone' : forms.CharField(max_length=256, required=True, help_text='',widget=forms.Select(attrs={'class': 'form-control'})),
    #'email' : forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'afoteyo@yahoo.com...'}),
    #'address' : forms.CharField(max_length=256, required=True, help_text='',widget=forms.Select(attrs={'class': 'form-control'})),

    #}




# class CreateCustomer(forms.ModelForm):
 #   name = forms.CharField(max_length=600, required=True, help_text='')

    # class Meta:
      #  model = Customer
     #   fields = ['name', 'phone', 'email', 'address']

class CreateBankInfo(forms.ModelForm):
    class Meta:
        model = BankInformation
        fields = ['name', 'bank_Short_Name']


class CreateBranchInfo(forms.ModelForm):
    class Meta:
        model = BranchInformation
        fields = ['branch_Name']


class CreateCompInfo(forms.ModelForm):
    class Meta:
        model = ComanyInformation
        fields = ['name', 'email', 'website', 'address',
                  'location', 'phone', 'customer_Service_Number',
                  'fax_number', 'VAT_Registration_Number'
                  ]

class CreateCompBankAccInfo(forms.ModelForm):
    class Meta:
        model = CompanyBankAccountInformation
        fields = ['name', 'account_Number', 'currency_Name']


class CreateCurrency(forms.ModelForm):
    class Meta:
        model = Currency
        fields = ['name', 'exchange_Rate']


class CreateInstallationCharge(forms.ModelForm):
    class Meta:
        model = InstallationCharge
        fields = ['area_Name', 'installation_Charge_Per_Meter',
                  'installation_percentage'
                  ]

class CreateInstallerInformation(forms.ModelForm):
    class Meta:
        model = InstallerInformation
        fields = ['name', 'phone']


class CreateMaterialColour(forms.ModelForm):
    class Meta:
        model = MaterialColourInformation
        fields = ['colour']

class CreateNarration(forms.ModelForm):
    class Meta:
        model = Narration
        fields = ['description']


class CreateotherTransDef(forms.ModelForm):
    class Meta:
        model = OtherTransactionDefinition
        fields = ['name']


class CreateprofileInfo(forms.ModelForm):
    class Meta:
        model = ProfileInformation
        fields = ['name', 'discount_Rate']

class CreatesalesMan(forms.ModelForm):
    class Meta:
        model = SalesManInformation
        fields = ['name', 'phone', 'initials']


class CreateserviceType(forms.ModelForm):
    class Meta:
        model = ServiceType
        fields = ['service_Type']


class CreateWarehouse(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ['name']
