from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(Request):
    '''This is a demo borrowed from tango with django
       it has absolutely no use here'''
    return HttpResponse("Davneet says I will fucking do it")
