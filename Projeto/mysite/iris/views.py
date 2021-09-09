from django.http import HttpResponse
from django.shortcuts import render
import requests
from .models import Iris
from .form import LoginForm
from rest_framework import routers, serializers, viewsets
from .serializer import IrisSerializer


def home(request):
    return render(request, 'Iris/base.html')


class IrisViewSet(viewsets.ModelViewSet):
    queryset = Iris.objects.all()
    serializer_class = IrisSerializer



def loginscreen(request):

    form = LoginForm(request.POST or None)

    username= ''
    password= ''

    if request.method == 'POST':

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']


    context = {
        'form':form,
        'username':username,
        'password':password,
    }


    return render(request, 'Iris/login.html',context)

