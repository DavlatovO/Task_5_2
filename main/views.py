from django.shortcuts import render
from . import models

def index(request):
    regions = models.Region.objects.all() 

    return render(request, 'index.html', {'regions':regions})