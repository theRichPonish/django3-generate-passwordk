from django.http import HttpResponse
from django.shortcuts import render
import random as software
# Create your views here.
def starter(request):
    return render(request, 'generate/about.html')
def passwordgenepage(request):
    return render(request, 'generate/test.html')
def passwordpage(request):
    thing = list('abcdefghijklmnopqrstuvwxyz')
    length = request.GET.get('length')
    thepassword = ''
    if request.GET.get('numbers'):
        thing.extend('0123456789')
    if request.GET.get('special'):
        thing.extend(')!@#$%^&*(\/.,><;:""?}{[]`~')
    if request.GET.get('uppercase'):
        thing.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('emoji'):
        thing.extend('😀😁😂🤣😃😄😥😅😆😉😊😋😎😍😘🥰😗😙😚☺🙂🤗🤩🤔🤨😐😑😶🙄😏😣😥😮🤐😯😪🎈🥠🥙🍠🦪🚔🚘🛹🚝🚞🚡')
    for z in range(int(length)):
        thepassword += software.choice(thing)
    return render(request, 'generate/passwordpage.html',{'password': thepassword})
