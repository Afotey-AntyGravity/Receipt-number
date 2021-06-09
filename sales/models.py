#from django.db import models
from proforma.models import *


# Create your models here.
#----------------Sales Receipt------------------------------->
#----------------Material Receipt------------------>
class MaterialReceipt(models.Model):
    MODE = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Transfer Pay', 'Transfer Pay'),
        ('Momo', 'Momo'),
    )


    reference_Number = models.CharField(max_length=200, null=True)
    branch_id = models.ManyToManyField(BranchInformation)
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    payment_Date = models.DateField()
    value_Date = models.DateField()
    withhold_Tax = models.BooleanField(default=True)
    cheque_Number = models.CharField(max_length=200, null=True)
    mode = models.CharField(max_length=200, null=True, choices=MODE)
    post_Dated_Cheque = models.BooleanField()
    customer_bank = models.ManyToManyField(BankInformation)
    cheque_Date = models.DateField(null=True)
    receipt_Number = models.CharField(max_length=200, null=True)
    currency = models.ManyToManyField(Currency)
    amount = models.FloatField(null=True)
    base_Amount = models.FloatField(null=True)
   #payment on proforma =
   #standar/longsheet/Trusses =
    proforma_Number = models.CharField(max_length=200, null=True)
   #accounts pay in number =
    narration = models.ManyToManyField(Narration)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.reference_Number



#----------------Point Of Sales Receipt------------------>
class PointofSalesReceipt(models.Model):
    reference_Number = models.CharField(max_length=200, null=True)
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    date = models.DateTimeField(default=timezone.now)
    sales_Officer = models.ForeignKey(SalesManInformation, null=True, on_delete= models.SET_NULL)
    currency = models.ForeignKey(Currency, null=True, on_delete= models.SET_NULL)
    discount_Rate = models.FloatField(null=True)
    #-----Second lock-------->
    product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
    material_Color = models.ForeignKey(MaterialColourInformation, null=True, on_delete= models.SET_NULL)
    unit_Price = models.FloatField(null=True)
    quantity = models.PositiveIntegerField(default=0)
    goods_Pending = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    #invoice Total
    #VAT %
    #total discount
    #total Payment
    #net balance

    def __str__(self):
        return self.reference_Number

#----------------Issue of Collected Items------------------>


#----------------Installation Payment Receipt------------------>
class InstallationPaymentReceipt(models.Model):

    MODE = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
    )
    reference_Number = models.CharField(max_length=200, null=True)
    PFI_Number = models.ForeignKey(ProformaReceipt, null=True, on_delete= models.SET_NULL)
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    installation_Amount = models.FloatField(null=True)
    amount_Paid = models.FloatField(null=True)
    exfactory_Amount = models.FloatField(null=True)
    commission_Charged = models.FloatField(null=True)
    date = models.DateTimeField(default=timezone.now)
    installer = models.ForeignKey(InstallerInformation, null=True, on_delete= models.SET_NULL)
    payment_Method = models.CharField(max_length=200, null=True, choices=MODE)
    cheque_Number = models.CharField(max_length=200, null=True)
    cheque_Date = models.DateTimeField(auto_now_add=True)
    customer_bank = models.ManyToManyField(BankInformation)
    currency = models.ForeignKey(Currency, null=True, on_delete= models.SET_NULL)
    #exchange Rate
    #base currency amount
    narration = models.ManyToManyField(Narration)

    def __str__(self):
        return self.reference_Number

#----------------Commssion Payment Receipt------------------>
class CommissionPaymentReceipt(models.Model):
    MODE = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Transfer Pay', 'Transfer Pay'),
        ('Momo', 'Momo'),
    )

    reference_Number = models.CharField(max_length=200, null=True)
    PFI_Number = models.ForeignKey(ProformaReceipt, null=True, on_delete= models.SET_NULL)
    invoice_Amount = models.FloatField(null=True)
    discount = models.ManyToManyField(DiscountTable)
    invoice_Discount = models.FloatField(null=True)
    initial_Pay = models.FloatField(null=True)
    difference = models.FloatField(null=True)
    maximum_Discount = models.FloatField(null=True)
    maximum_Discount_Paid = models.FloatField(null=True)
    commission_Retained = models.FloatField(null=True)
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True)
    recepient_Name = models.CharField(max_length=200, null=True)
    phone_Number = models.CharField(max_length=200, null=True)
    mode = models.CharField(max_length=200, null=True, choices=MODE)
    cheque_Number = models.CharField(max_length=200, null=True)
    cheque_Date = models.DateTimeField(auto_now_add=True)
    customer_bank = models.ManyToManyField(BankInformation)
    currency = models.ForeignKey(Currency, null=True, on_delete= models.SET_NULL)
    #exchange Rate
    amount = models.FloatField(null=True)
    base_Amount = models.FloatField(null=True)
    narration = models.ManyToManyField(Narration)
    #item batch
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return self.reference_Number

#----------------Bank Pay in/Expenses------------------>
class Expenses(models.Model):
    CHOICE = (
        ('Bank Pay In', 'Bank Pay In'),
        ('Expenses', 'Expenses'),
    )

    MODE = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
    )

    reference_Number = models.CharField(max_length=200, null=True)
    payment_date = models.DateTimeField(default=timezone.now)
    choice = models.CharField(max_length=200, null=True, choices=CHOICE)
    mode = models.CharField(max_length=200, null=True, choices=MODE)
    cheque_Number = models.CharField(max_length=200, null=True)
    account_Number = models.CharField(max_length=200, null=True)
    customer_bank = models.ManyToManyField(BankInformation)
    currency = models.ForeignKey(Currency, null=True, on_delete= models.SET_NULL)
    amount = models.PositiveIntegerField()
    narration = models.ManyToManyField(Narration)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.reference_Number
