from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import LoginValidator


def login_page(request):
    # context = {'login': 'Enter your login'}
    return render(request, 'TestTask/LoginPage.html')


def validate_login_page(request):
    if request.method == 'POST':
        login = request.POST.get('login_field', '')
        if LoginValidator.is_login_valid(login):
            return HttpResponse("Entered login is correct.<br>Go <a href='/testtask'>back</a>.")
        else:
            return HttpResponse("Entered login is not correct.<br>Go <a href='/testtask'>back</a>.")
    else:
        return HttpResponseRedirect('/testtask/')


def scheme_page(request):
    context = {'fillColor': '#E3EBF5', 'mouseoverColor': 'green'}
    return render(request, 'TestTask/Scheme.html', context)