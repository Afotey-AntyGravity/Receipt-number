from django.contrib import admin
from .models import *
# Register your models here.


class MaterialReceiptAdmin(admin.ModelAdmin):
    list_display = ('id', 'reference_Number', 'date_created')
    list_filter = ('reference_Number', 'date_created')

admin.site.register(MaterialReceipt, MaterialReceiptAdmin)


class ProformaReceiptAdmin(admin.ModelAdmin):
    list_display = ('id', 'reference_Number', 'customer', 'date_created', 'updated')
    list_filter = ('customer', 'date_created')

admin.site.register(ProformaReceipt, ProformaReceiptAdmin)


class PointofSalesReceiptAdmin(admin.ModelAdmin):
    list_display = ('id', 'reference_Number', 'customer', 'date_created', 'updated')
    list_filter = ('customer', 'date_created')

admin.site.register(PointofSalesReceipt, PointofSalesReceiptAdmin)


class CommissionPaymentReceiptAdmin(admin.ModelAdmin):
    list_display = ('id', 'reference_Number', 'customer', 'date_created', 'updated')
    list_filter = ('customer', 'date_created')

admin.site.register(CommissionPaymentReceipt, CommissionPaymentReceiptAdmin)


class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('id', 'reference_Number', 'payment_date', 'date_created', 'updated')
    list_filter = ('payment_date', 'date_created')

admin.site.register(Expenses, ExpensesAdmin)
