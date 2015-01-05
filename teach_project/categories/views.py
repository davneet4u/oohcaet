from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    '''This is a demo borrowed from tango with django
       it has absolutely no use here'''
    context_dict={'message':'Keep up the pace bro'}
    return render(request,'index.html',context_dict)

