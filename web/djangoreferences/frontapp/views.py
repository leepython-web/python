from django.shortcuts import render

def index_page(request):
    return render(request, 'index.html')

def heroes(request):
    return render(request, 'heroes.html')
