from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def calculate(request):
    if request.method=="GET":
        return render(request, "calculate.html")
    elif request.method=="POST":
        option=request.POST["operation"]
        if option=="a":
            
            val1 =int(request.POST["num1"])
            val2 =int(request.POST["num2"])
            add_val=val1+val2
            return render(request, "calculate.html", {"value":add_val})
        if option=="s":
            val1 =int(request.POST["num1"])
            val2 =int(request.POST["num2"])
            sub_val=val1-val2
            return render(request, "calculate.html", {"value":sub_val})

        
        