from django.contrib import admin

# Register your models here.
from .models import *


class BankInformationAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'bank_Short_Name', 'date_created')
    list_filter = ('name', 'date_created')

admin.site.register(BankInformation, BankInformationAdmin)

class CompanyInformationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'location', 'VAT_Registration_Number')

admin.site.register(BranchInformation)

admin.site.register(ComanyInformation, CompanyInformationAdmin)

class TaxInformationAdmin(admin.ModelAdmin):
    list_display = ('name', 'VAT_Rate', 'date_created')

admin.site.register(TaxtableInformation, TaxInformationAdmin)

class CompanyBankAccountInformationAdmin(admin.ModelAdmin):
    list_display = ('name', 'account_Number', 'date_created')
    list_filter = ('name', 'date_created')

admin.site.register(CompanyBankAccountInformation, CompanyBankAccountInformationAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'exchange_Rate', 'date_created')

admin.site.register(Currency, CurrencyAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'address')

admin.site.register(Customer, CustomerAdmin)

class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')

admin.site.register(Description, DescriptionAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'profile_code')
    list_filter = ('name', 'price')

admin.site.register(Product, ProductAdmin)

admin.site.register(Order)

class InstallationChargeAdmin(admin.ModelAdmin):
    list_display = ('area_Name', 'installation_Charge_Per_Meter', 'installation_percentage')

admin.site.register(InstallationCharge, InstallationChargeAdmin)


class InstallerInformationAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created')

admin.site.register(InstallerInformation, InstallerInformationAdmin)


class MaterialTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'division_Constant')

admin.site.register(MaterialType, MaterialTypeAdmin)


class MaterialColourInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'colour')


admin.site.register(MaterialColourInformation, MaterialColourInformationAdmin)

class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ('service_Type', 'date_created')
    list_filter = ('service_Type', 'date_created')

admin.site.register(ServiceType, ServiceTypeAdmin)


class OtherTransactionDefinitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created')

admin.site.register(OtherTransactionDefinition, OtherTransactionDefinitionAdmin)


admin.site.register(Narration)


class SalesManInformationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'initials')

admin.site.register(SalesManInformation, SalesManInformationAdmin)


class ProfileInformationAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount_Rate')

admin.site.register(ProfileInformation, ProfileInformationAdmin)


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created')

admin.site.register(Warehouse, WarehouseAdmin)

admin.site.register(Tax)

class DiscountTableAdmin(admin.ModelAdmin):
    list_display = ('start_Limit', 'end_Limit', 'discount_Rate', 'date_created', 'updated')
    list_filter = ('date_created', 'updated')

admin.site.register(DiscountTable)

