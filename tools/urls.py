from django.urls import path

from .import views

app_name = 'tools'
urlpatterns = [
    path('', views.setup, name='tools'),

    path('BankInfo/', views.bankInfo, name="bank_information"),
    path('BankInfoform/', views.bankInfoform, name="bank_info_form"),
    path('update_BankInfo/<str:pk_two>/', views.updateBankInfo, name="update_bank_info"),

    path('branchInfo/', views.branchInfo, name="branch_information"),
    path('branchInfoform/', views.branchInfoform, name="branch_info_form"),
    path('update_branchInfo/<str:pk_three>/', views.updatebranchInfo, name="update_branch_info"),

    path('TaxInfo/', views.taxInfo, name="tax_information"),

    path('CompanyInfo/', views.companyInfo, name="company_information"),
    path('CompanyInfoform/', views.companyInfoform, name="comp_info_form"),
    path('update_CompInfo/<str:pk_four>/', views.updatecompanyInfo, name="update_comp_info"),

    path('customer/', views.customer, name="customer"),
    path('customerlist/<str:pk_test>/', views.customerlist, name="customer_list"),
    path('create_customer/', views.createCustomer, name="create_customer"),
    path('update_customer/<str:pk_one>/', views.updateCustomer, name="update_customer"),

    path('products/', views.products, name="products"),


    path('serviceType/', views.serviceType, name="service_type_information"),
    path('create_serviceType/', views.createserviceType, name="create_service_type_information"),
    path('update_serviceType/<str:pk_fourt>/', views.updateserviceType, name="update_service_type_information"),

    path('currency/', views.currency, name="currency"),
    path('currencyform/', views.currencyform, name="currency_form"),
    path('update_currency/<str:pk_six>/', views.updatecurrency, name="update_currency"),

    path('compBankAccInfo/', views.compBankAccInfo, name="company_bank_account_information"),
    path('compBankAccInfoform/', views.compBankAccInfoform, name="company_bank_account_form"),
    path('update_compBankAccInfo/<str:pk_five>/', views.updatecompBankAccInfo, name="update_company_bank_account_info"),

    path('otherTransDef/', views.otherTransDef, name="other_transaction_definition"),
    path('create_otherTransDef/', views.createotherTransDef, name="create_other_transaction_definition"),
    path('update_otherTransDef/<str:pk_eleven>/', views.updateotherTransDef, name="update_other_transaction_definition"),

    path('narration/', views.narration, name="narration"),
    path('create_narration/', views.createnarration, name="create_narration"),
    path('update_narration/<str:pk_ten>/', views.updatenarration, name="update_narration"),

    path('warehouse/', views.warehouse, name="warehouse"),
    path('create_warehouse/', views.createwarehouse, name="create_warehouse"),
    path('update_warehouse/<str:pk_fift>/', views.updatewarehouse, name="update_warehouse"),

    path('salesManInfo/', views.salesManInfo, name="sales_man_information"),
    path('salesManInfolist/<str:pk_sales>/', views.salesManInfolist, name="salesManInfolist"),
    path('create_salesMan/', views.createsalesMan, name="create_salesMan"),
    path('update_salesMan/<str:pk_thirt>/', views.updatesalesMan, name="update_salesMan"),

    path('matColourInfo/', views.matColourInfo, name="material_colour_information"),
    path('create_matColourInfo/', views.creatematColourInfo, name="create_material_colour_information"),
    path('update_matColourInfo/<str:pk_nine>/', views.updateColourInfo, name="update_material_colour_information"),

    path('installationCharge/', views.installationCharge, name="installation_charge"),
    path('create_installationCharge/', views.createinstallationcharge, name="create_installation_charge"),
    path('update_installationCharge/<str:pk_seven>/', views.updateinstallationcharge, name="update_installation_charge"),

    path('profileInfo/', views.profileInfo, name="profile_information"),
    path('create_profileInfo/', views.createprofileInfo, name="create_profile_information"),
    path('update_profileInfo/<str:pk_twelve>/', views.updateprofileInfo, name="update_profile_information"),

    path('installerInfo/', views.installerInfo, name="installer_information"),
    path('installerInfolist/<str:pk_inst>/', views.installerInfolist, name="installer_list"),
    path('create_installerInfo/', views.createinstallerInfo, name="create_installer_info"),
    path('update_installerInfo/<str:pk_eight>/', views.updateinstallerInfo, name="update_installer_info"),

]
