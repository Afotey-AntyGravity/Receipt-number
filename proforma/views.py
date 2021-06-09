from django.shortcuts import render, redirect

# Create your views here.
from .models import *
from .forms import *

import random
import datetime


def proformaview(request):

    return render(request, 'proforma/proformareceipt.html')


def proformastandard(request):
    ProformaStandard = ProformaReceipt.objects.all()

    context = {'ProformaStandard': ProformaStandard}
    return render(request, 'proforma/proforma_standard.html', context)

def createproformastandard(request):

    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day

    if len(str(day)) == 1:
        day = "0" + str(day)
    if len(str(month)) == 1:
        month = "0" + str(month)

    today = str(year) + "/" + str(month) + "/" + str(day)

    date = str(year) + str(month) + str(day)
    randint = str(random.randint(1000, 9999))
    rand = str("TSCL") + date + "-" + randint + str("-P")
    rand = str(rand)

    while len(ProformaReceipt.objects.filter(rand=rand)) != 0:
        randint = str(random.randint(1000, 9999))
        rand = date + randint
        rand = int(rand)

    form = CreateProformaReceipt()
    if request.method == 'POST':
        form = CreateProformaReceipt(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'proforma/proforma_form_standard.html', context)
