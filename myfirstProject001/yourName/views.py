from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#we add request to recieve incoming request from url
def yournamedetial(request): 
    return HttpResponse("My Name is Shibli Nomani. And I am currently studying Django")
