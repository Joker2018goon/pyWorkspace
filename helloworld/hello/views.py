from django.shortcuts import render
from django.http import HttpResponse
import models

# Create your views here.
def index(request):
    article1=models.Article.objects.get(pk=1)
    article2 = models.Article.objects.get(pk=2)
    return render(request, 'hello/index.html',{'article1':article1,'article2':article2})