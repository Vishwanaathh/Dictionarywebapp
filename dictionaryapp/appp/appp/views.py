from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
def home(request):
    return render(request,'home.html')
def mean(request):
    wordd=request.GET["word"]
    url="https://api.dictionaryapi.dev/api/v2/entries/en/"+wordd
    response=requests.get(url)
    data=response.json()
    meaning=data[0]['meanings'][0]['definitions'][0]['definition']

    return render(request,'mean.html',{"meaning":meaning})
