from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def setup(request):

    return render(request, 'tools/setup.html')

def bankInfo(request):
    bank = BankInformation.objects.all()

    context = {'bank': bank}
    return render(request, "tools/BankInfo.html", context)

def bankInfoform(request):

    form = CreateBankInfo()
    if request.method == 'POST':
        form = CreateBankInfo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, "tools/BankInfo_form.html", context)

def updateBankInfo(request, pk_two):

    update = BankInformation.objects.get(id=pk_two)
    form = CreateBankInfo(instance=update)

    if request.method == 'POST':
        form = CreateBankInfo(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, "tools/BankInfo_form.html", context)


def branchInfo(request):
    branch = BranchInformation.objects.all()

    context = {'branch': branch}
    return render(request, 'tools/branchInfo.html', context)

def branchInfoform(request):

    form = CreateBranchInfo()
    if request.method == 'POST':
        form = CreateBranchInfo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, "tools/branchInfo_form.html", context)


def updatebranchInfo(request, pk_three):

    update = BranchInformation.objects.get(id=pk_three)
    form = CreateBranchInfo(instance=update)

    if request.method == 'POST':
        form = CreateBranchInfo(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, "tools/branchInfo_form.html", context)


def companyInfo(request):
    compInfo = ComanyInformation.objects.all()

    context =  {'compInfo': compInfo}
    return render(request, 'tools/companyInfo.html', context)

def companyInfoform(request):

    form = CreateCompInfo()
    if request.method == 'POST':
        form = CreateCompInfo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, "tools/compInfo_form.html", context)

def updatecompanyInfo(request, pk_four):

    update = ComanyInformation.objects.get(id=pk_four)
    form = CreateCompInfo(instance=update)

    if request.method == 'POST':
        form = CreateCompInfo(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, "tools/compInfo_form.html", context)


def compBankAccInfo(request):
    compBankInfo = CompanyBankAccountInformation.objects.all()

    context = {'compBankInfo': compBankInfo}
    return render(request, 'tools/compBankAccInfo.html', context)

def compBankAccInfoform(request):

    form = CreateCompBankAccInfo()
    if request.method == 'POST':
        form = CreateCompBankAccInfo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'tools/compBankAccInfo_form.html', context)


def updatecompBankAccInfo(request, pk_five):

    update = CompanyBankAccountInformation.objects.get(id=pk_five)
    form = CreateCompBankAccInfo(instance=update)

    if request.method == 'POST':
        form = CreateCompBankAccInfo(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'tools/compBankAccInfo_form.html', context)


def currency(request):
    currency = Currency.objects.all()

    context = {'currency': currency}
    return render(request, 'tools/currency.html', context)

def currencyform(request):

    form = CreateCurrency()
    if request.method == 'POST':
        form = CreateCurrency(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'tools/currency_form.html', context)

def updatecurrency(request, pk_six):

    update = Currency.objects.get(id=pk_six)
    form = CreateCurrency(instance=update)

    if request.method == 'POST':
        form = CreateCurrency(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'tools/currency_form.html', context)



def customer(request):
    customer = Customer.objects.all()

    context = {'customer': customer}
    return render(request, 'tools/customer.html', context)

def customerlist(request, pk_test):
    customerlist = Customer.objects.get(id=pk_test)

    context = {'customerlist': customerlist}
    return render(request, 'tools/customerlist.html', context)

def createCustomer(request):

    form = CreateCustomer()
    if request.method == 'POST':
        form = CreateCustomer(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

   # if request.method=="POST":
    #    contact = Customer()
     #   name = request.POST.get('name')
      #  phone = request.POST.get('phone')
       # email = request.POST.get('email')
       # address = request.POST.get('address')
     #   contact.name = name
     #   contact.phone = phone
     #   contact.email = email
     #   contact.address = address
     #   contact.save()
     #   return redirect('/')

    context = {'form': form}
    return render(request, 'tools/create_customer.html', context)

def updateCustomer(request, pk_one):

    update = Customer.objects.get(id=pk_one)
    form = CreateCustomer(instance=update)

  #  if request.method=="POST":
  #      contact = Customer(instance=update)
  #      name = request.POST.get('name')
  #      phone = request.POST.get('phone')
  #      email = request.POST.get('email')
  #      address = request.POST.get('address')
  #      contact.name = name
  #      contact.phone = phone
  #     contact.email = email
  #      contact.address = address
  #      contact.save()
  #      return redirect('/')
    if request.method == 'POST':
        form = CreateCustomer(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'tools/create_customer.html', context)


def products(request):
    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'tools/tools_create/products.html', context)

def serviceType(request):
    service = ServiceType.objects.all()

    context = {'service': service}
    return render(request, 'tools/serviceType.html', context)


def createserviceType(request):

    form = CreateserviceType()
    if request.method == 'POST':
        form = CreateserviceType(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'tools/serviceType_form.html', context)


def updateserviceType(request, pk_fourt):

    update = ServiceType.objects.get(id=pk_fourt)
    form = CreateserviceType(instance=update)

    if request.method == 'POST':
        form = CreateserviceType(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'tools/serviceType_form.html', context)


def installerInfo(request):
    installer = InstallerInformation.objects.all()

    context = {'installer': installer}
    return render(request, 'tools/installerInfo.html', context)


def installerInfolist(request, pk_inst):

    installerinfolist = InstallerInformation.objects.get(id=pk_inst)

    context = {'installerinfolist': installerinfolist}
    return render(request, 'tools/installerInfolist.html', context)

def createinstallerInfo(request):

    form = CreateInstallerInformation()
    if request.method == 'POST':
        form = CreateInstallerInformation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'tools/installerInfo_form.html', context)

def updateinstallerInfo(request, pk_eight):

    update = InstallerInformation.objects.get(id=pk_eight)
    form = CreateInstallerInformation(instance=update)

    if request.method == 'POST':
        form = CreateInstallerInformation(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'tools/installerInfo_form.html', context)

def otherTransDef(request):
    othertrans = OtherTransactionDefinition.objects.all()

    context = {'othertrans': othertrans}
    return render(request, 'tools/otherTransDef.html', context)

def createotherTransDef(request):

    form = CreateotherTransDef()
    if request.method == 'POST':
        form = CreateotherTransDef(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'tools/otherTransDef_form.html', context)

def updateotherTransDef(request, pk_eleven):

    update = OtherTransactionDefinition.objects.get(id=pk_eleven)
    form = CreateotherTransDef(instance=update)

    if request.method == 'POST':
        form = CreateotherTransDef(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'tools/otherTransDef_form.html', context)

def narration(request):
    narration = Narration.objects.all()

    context = {'narration': narration}
    return render(request, 'tools/narration.html', context)


def createnarration(request):

    form = CreateNarration()
    if request.method == 'POST':
        form = CreateNarration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'tools/narration_form.html', context)

def updatenarration(request, pk_ten):

    update = Narration.objects.get(id=pk_ten)
    form = CreateNarration(instance=update)

    if request.method == 'POST':
        form = CreateNarration(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'tools/narration_form.html', context)




def warehouse(request):
    warehouse = Warehouse.objects.all()

    context = {'warehouse':warehouse}
    return render(request, 'tools/warehouse.html', context)

def createwarehouse(request):

    form = CreateWarehouse()
    if request.method == 'POST':
        form = CreateWarehouse(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'tools/warehouse_form.html', context)

def updatewarehouse(request, pk_fift):

    update = Warehouse.objects.get(id=pk_fift)
    form = CreateWarehouse(instance=update)

    if request.method == 'POST':
        form = CreateWarehouse(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'tools/warehouse_form.html', context)

def salesManInfo(request):
    salesman = SalesManInformation.objects.all()

    context = {'salesman': salesman}
    return render(request, 'tools/salesManInfo.html', context)

def salesManInfolist(request, pk_sales):

    salesmanlist = SalesManInformation.objects.get(id=pk_sales)

    context = {'salesmanlist': salesmanlist}
    return render(request, 'tools/salesManInfolist.html', context)

def createsalesMan(request):

    form = CreatesalesMan()
    if request.method == 'POST':
        form = CreatesalesMan(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'tools/salesMan_form.html', context)

def updatesalesMan(request, pk_thirt):

    update = SalesManInformation.objects.get(id=pk_thirt)
    form = CreatesalesMan(instance=update)

    if request.method == 'POST':
        form = CreatesalesMan(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'tools/salesMan_form.html', context)


def matColourInfo(request):
    matcolour = MaterialColourInformation.objects.all()

    context = {'matcolour': matcolour}
    return render(request, 'tools/matColourInfo.html', context)

def creatematColourInfo(request):

    form = CreateMaterialColour()
    if request.method == 'POST':
        form = CreateMaterialColour(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form': form}
    return render(request, 'tools/matColourInfo_form.html', context)

def updateColourInfo(request, pk_nine):

    update = MaterialColourInformation.objects.get(id=pk_nine)
    form = CreateMaterialColour(instance=update)

    if request.method == 'POST':
        form = CreateMaterialColour(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'tools/matColourInfo_form.html', context)

def installationCharge(request):
    installcharge = InstallationCharge.objects.all()

    context = {'installcharge': installcharge}
    return render(request, 'tools/installationCharge.html', context)


def createinstallationcharge(request):

    form = CreateInstallationCharge()
    if request.method == 'POST':
        form = CreateInstallationCharge(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'tools/installationCharge_form.html', context)

def updateinstallationcharge(request, pk_seven):

    update = InstallationCharge.objects.get(id=pk_seven)
    form = CreateInstallationCharge(instance=update)

    if request.method == 'POST':
        form = CreateInstallationCharge(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'tools/installationCharge_form.html', context)


def profileInfo(request):
    profile = ProfileInformation.objects.all()

    context = {'profile': profile}
    return render(request, 'tools/profileInfo.html', context)


def createprofileInfo(request):

    form = CreateprofileInfo()
    if request.method == 'POST':
        form = CreateprofileInfo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'tools/profileInfo_form.html', context)

def updateprofileInfo(request, pk_twelve):

    update = ProfileInformation.objects.get(id=pk_twelve)
    form = CreateprofileInfo(instance=update)

    if request.method == 'POST':
        form = CreateprofileInfo(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'tools/profileInfo_form.html', context)

def taxInfo(request):
    taxesInfo = TaxtableInformation.objects.all()

    context = {'taxesInfo': taxesInfo}
    return render(request, 'tools/taxInfo.html', context)
