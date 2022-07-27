
from urllib import request
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse

# Create your views here.
def home(request):

      return render(request, "home/home.html")

