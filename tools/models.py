from django.db import models

# Create your models here.

#1 ----------------Bank Informtation------------------>
class BankInformation(models.Model):
    name = models.CharField(max_length=200, null=True)
    bank_Short_Name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


#2 ----------------Branch Informtation------------------>
class BranchInformation(models.Model):
    branch_Name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.branch_Name

#3 ----------------Company Bank Account Informtation------------------>
class CompanyBankAccountInformation(models.Model):
    name = models.CharField(max_length=200, null=True)
    account_Number = models.PositiveIntegerField(null=True)
    currency_Name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

#4----------------Company Informtation------------------>
class ComanyInformation(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    website = models.CharField(max_length=200, null=True)
    address   = models.CharField(max_length=200, null=True)
    location  = models.CharField(max_length=200, null=True)
    phone     = models.CharField(max_length=200, null=True)
    customer_Service_Number = models.CharField(max_length=200, null=True)
    fax_number = models.CharField(max_length=200, null=True)
    VAT_Registration_Number = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

#5----------------Currency Informtation------------------>
class Currency(models.Model):
    name = models.CharField(max_length=200, null=True)
    exchange_Rate = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

#6----------------Customer Informtation------------------>
class Customer(models.Model):
    name  = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

  #  def get_absolute_url(self):
   #     return f"/customerlist/{self.id}"


#7------------------Product Description-------------------------->
class Description(models.Model):
    name = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.name


#8----------------Product Informtation------------------>
class Product(models.Model):

    name = models.CharField(max_length=300, null=True)
    price = models.FloatField(null=True)
    descriptions = models.ManyToManyField(Description) #category info has been added to product info
    category = models.CharField(max_length=300, null=True)
    profile_code = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

#9----------------Create Proforma or Order------------------>
class Order(models.Model):


    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    product  = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True)
    note   = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.product.name

#10----------------Installation Charge------------------>
class InstallationCharge(models.Model):
    area_Name = models.CharField(max_length=200,null=True)
    installation_Charge_Per_Meter = models.FloatField(null=True)
    installation_percentage = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.area_Name

#11----------------Installer Informtation------------------>
class InstallerInformation(models.Model):
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

#12----------------Material Type Informtation------------------>
class MaterialType(models.Model):
    name = models.CharField(max_length=200, null=True)
    division_Constant = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


#13----------------Material Colour Informtation------------------>
class MaterialColourInformation(models.Model):
   #name = models.CharField(max_length=200,null=True)
    colour = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.colour


#14----------------Tax Informtation------------------>
class TaxtableInformation(models.Model):
    name  = models.CharField(max_length=200, null=True)
    VAT_Rate = models.FloatField(null=True)
    GET_Fund_Rate = models.FloatField(null=True)
    NHIL_Rate = models.FloatField(null=True)
    VAT_Flat_Rate =models.FloatField(null=True)
    Installation_Retention_Rate = models.FloatField(null=True)
    Discount_Rate = models.FloatField(null=True)
    Maximum_Discount_Rate = models.FloatField(null=True)
    Commission_Retention = models.FloatField(null=True)
    Maximum_Commission = models.DecimalField(max_length=200, max_digits=1000, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name


#15----------------Service Type Informtation------------------>
class ServiceType(models.Model):
    service_Type = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.service_Type



#16----------------Other Transaction Definition------------------>
class OtherTransactionDefinition(models.Model):
    name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

#17----------------Narration------------------>
class Narration(models.Model):
    description = models.CharField(max_length=1000,null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.description


#18----------------SalesMan Information------------------>
class SalesManInformation(models.Model):
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200, null=True)
    initials = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name



#19----------------Profile Informtation------------------>
class ProfileInformation(models.Model):
    name = models.CharField(max_length=200,null=True)
    discount_Rate = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

#19----------------VAT/GET Fund/NHIL Information------------------>
class Tax(models.Model):
    vat_Percentage = models.FloatField(null=True)
    GET_Fund_Percentage = models.FloatField(null=True)
    NHIL_Percentage = models.FloatField(null=True)
    VAT_Flat_Percentage = models.FloatField(null=True)
    Installation_Retention = models.FloatField(null=True)
    discount_Rate = models.FloatField(null=True)
    Maximum_Discount_Rate = models.FloatField(null=True)
    Commission_Retention = models.FloatField(null=True)
    maximum_Retention = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

#20----------------Warehouse ------------------>
class Warehouse(models.Model):
    name = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

#22----------------Discount Table------------------>
class DiscountTable(models.Model):
    discount_Rate = models.FloatField(null=True)
    start_Limit = models.FloatField(null=True)
    end_Limit = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
