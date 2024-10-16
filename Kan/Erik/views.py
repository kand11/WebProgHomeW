from django.shortcuts import render
from django.http import HttpResponse
def name(request):
    return HttpResponse('Erik')
def group(request):
    return HttpResponse('БИН-22-2')
def age(request):
    return HttpResponse('21 y.o.')
def common(request):
    return HttpResponse('Erik, БИН-22-2, 21 y.o.')
# Create your views here.
