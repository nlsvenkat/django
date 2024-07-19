from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.
def add(request):
    return render(request, "add.html")

def result(request):
    if request.method=="POST":
        val1=request.POST['num1']
        val2=request.POST['num2']
        val3=val1+val2
        return render(request,"result.html",{"value":val3})
    return render(request,"result.html",{"value":""})

def quiz(request):
    answers_list=["o1","o2"]
    if request.method=="POST":
        val1=request.POST['q1']
        val2=request.POST['q2']
        given_list=[val1,val2]
        score=0
        for i in range(len(answers_list)):
            if(answers_list[i]==given_list[i]):
                score+=1
        return render(request,"quiz.html",{"score":score})
    return render(request,"quiz.html",{"score":""})
    
    