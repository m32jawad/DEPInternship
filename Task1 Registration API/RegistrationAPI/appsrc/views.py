from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt 
def add_record(request):
    
    pass