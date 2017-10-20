from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect

def index(request):
    response= "Placeholder to later display all the list of blogs"
    return HttpResponse(response)

def indexBlogs(request):
    response="Welcome to Blogs"
    return HttpResponse(response)

def new(request):
    return HttpResponse("Placeholder to display a new form to create a blog")

def create(request):
    return HttpResponseRedirect('/blogs')

def show(request,number):
    return HttpResponse("Placeholder to display blog " + number)

def edit(request,number):
    return HttpResponse("Placeholder to edit blog " + number)

def destroy(request,number):
    return HttpResponseRedirect('/blogs')
