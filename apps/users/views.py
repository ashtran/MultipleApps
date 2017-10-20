from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect

def index(request):
    response="Placeholder to later display alll the list of users"
    return HttpResponse(response)

def new(request):
    response="Placeholder to display a new form to create a new user record"
    return HttpResponse(response)

def show(request):
    response="Placeholder for users to login"
    return HttpResponse(response)
