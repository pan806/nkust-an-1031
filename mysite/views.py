from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def index(request):
    iucky_no = random.randint(1,42)
    numbers = []
    for i in range(6):  
        numbers.append(random.randint(1,42))

    return render(request, "index.html",locals())
