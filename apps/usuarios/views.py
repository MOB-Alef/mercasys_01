"""
=====================================================
PROJETO: MercaSys
ARQUIVO: views.py
STATUS: EM DESENVOLVIMENTO
=====================================================

OBJETIVO:
Controlar autenticação e páginas de usuários.
=====================================================
"""

from django.shortcuts import render, redirect

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .forms import CadastroUsuarioForm


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('email')
        senha = request.POST.get('senha')

        usuario = authenticate(
            request,
            username=username,
            password=senha
        )

        if usuario:

            login(request, usuario)

            messages.success(
                request,
                'Login realizado com sucesso!'
            )

            return redirect('dashboard')

        else:

            messages.error(
                request,
                'Email ou senha inválidos.'
            )

    return render(request, 'usuarios/login.html')


def cadastro_view(request):

    form = CadastroUsuarioForm()

    if request.method == 'POST':

        form = CadastroUsuarioForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Usuário cadastrado com sucesso!'
            )

            return redirect('login')

    context = {
        'form': form
    }

    return render(
        request,
        'usuarios/cadastro.html',
        context
    )


@login_required
def dashboard_view(request):

    return render(
        request,
        'usuarios/dashboard.html'
    )


def logout_view(request):

    logout(request)

    messages.success(
        request,
        'Logout realizado com sucesso!'
    )

    return redirect('login')