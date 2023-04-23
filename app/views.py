from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def insert_Topic(request):
    tob=Topicform()
    d={'tob':tob}
    if request.method=='POST':
        tof=Topicform(request.POST)
        if tof.is_valid():
            tof.save()
        return HttpResponse('topic is sumited successfully')
    return render(request,'insert_Topic.html',d)
def insert_Webpage(request):
    wob=Webpageform()
    d={'wob':wob}
    if request.method=='POST':
        wof=Webpageform(request.POST)
        if wof.is_valid():
            wof.save()
        return HttpResponse('webpage is submited successfully')
    return render(request,'insert_Webpage.html',d)
def insert_AccessRecord(request):
    Aob=AccessRecordform()
    d={'Aob':Aob}
    if request.method=='POST':
        Aof=AccessRecordform(request.POST)
        if Aof.is_valid():
            Aof.save()
        return HttpResponse('accessrecord is submited succefully')
    return render(request,'insert_AccessRecord.html',d)
    