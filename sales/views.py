from django.shortcuts import render
import random
import datetime
# Create your views here.

from .models import *

def referenceview(request):

    return render(request, 'sales/salesreceipt.html')
