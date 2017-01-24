from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context = { 'name': 'Name goes here',
            'date': 'January 23rd, 2017'}
    return render(request, 'index.html', context)
