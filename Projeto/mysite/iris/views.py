from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
from .models import Iris
from .form import LoginForm,RegisterForm
from rest_framework import routers, serializers, viewsets
from .serializer import IrisSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
import numpy as np
from ellipticcurve.ecdsa import Ecdsa
from ellipticcurve.privateKey import PrivateKey

from fnc.Iris import Olho


def home(request):
    return render(request, 'Iris/base.html')


class IrisViewSet(viewsets.ModelViewSet):
    queryset = Iris.objects.all()
    serializer_class = IrisSerializer

    @api_view(['GET', 'POST','DELETE'])
    def iris_list(request):
        """
        List all code snippets, or create a new snippet.
        """
        if request.method == 'GET':
            iris = Iris.objects.all()
            serializer = IrisSerializer(iris, many=True)
            return JsonResponse(serializer.data, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)

            privateKey = PrivateKey()
            publicKey = privateKey.publicKey()

            data['chave_privada'] = privateKey.toString()
            data['chave_publica'] = publicKey.toString()

            var_caminho = r"E:\TCCIRIS\Projeto\mysite\iris\image_iris\\" + data['upload']
            olho_temp = Olho( var_caminho)
            print(olho_temp.caminho)
            iris_temp = olho_temp.extrairCodigo()
            print(iris_temp)
            data['iris_codep1'] = np.array_str(iris_temp[0])
            data['iris_codep2'] = np.array_str(iris_temp[1])


            serializer = IrisSerializer(data=data)
    
            
            

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        elif request.method == 'DELETE':
            
            iris = Iris.objects.all().delete()
            return HttpResponse(status=204)




    @api_view(['GET', 'PUT', 'DELETE'])
    def iris_detail(request, pk):
        """
        Retrieve, update or delete a code snippet.
        """
        try:
            iris = Iris.objects.get(pk=pk)
        except Iris.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = IrisSerializer(iris)
            return JsonResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = IrisSerializer(iris, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            iris.delete()
            return HttpResponse(status=204)


def loginScreen(request):

        form = LoginForm(request.POST or None)

        username= ''
        password= ''
        chave_privada=''
        if request.method == 'POST':

            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                chave_privada = form.cleaned_data['chave_privada']
                
            
        context = {
            'form':form,
            'username':username,
            'password':password,
            'chave_privada':chave_privada
            
        }

        print(username,password,chave_privada)

        return render(request, 'Iris/login.html',context)


def registerScreen(request):

    form = RegisterForm(request.POST or None)

    nome = ''
    username= ''
    password= ''

    if request.method == 'POST':

        if form.is_valid():
            nome = form.cleaned_data['nome']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']


    context = {
        'form':form,
        'nome':nome,
        'username':username,
        'password':password,

    }


    return render(request, 'Iris/cadastro.html',context)

