from django.shortcuts import render

# Create your views here.

def waybillview(request):

    return render(request, 'waybill/waybill.html')
