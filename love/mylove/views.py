from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.cache import cache_page

@cache_page(60 * 5)
def index(request):
    return render(request, 'iloveu.html')