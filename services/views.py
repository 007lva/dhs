# -*- coding: utf-8 -*- 
from django.http import HttpResponse
import datetime

def home(request):
    return HttpResponse("tengo sueño csm")
