from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def safat(request):
    return HttpResponse("Hello This Is Book app")