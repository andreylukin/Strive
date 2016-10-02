from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#

def index(request):
    return HttpResponse("Lets get this show on the road")


