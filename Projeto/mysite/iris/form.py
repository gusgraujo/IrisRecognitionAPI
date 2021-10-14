from django import forms

class LoginForm(forms.Form):
    usuario = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100)
    chave_privada = forms.CharField(label='Chave_privada', max_length=100)
    imgIris = forms.CharField(label='img', max_length=100)


class RegisterForm(forms.Form):
    nome = forms.CharField(label='nome', max_length=100)
    password = forms.CharField(label='Password', max_length=100)
    imgIris = forms.CharField(label='img', max_length=100)
