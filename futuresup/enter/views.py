from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'enter/enter_page.html')