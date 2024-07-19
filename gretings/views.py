from django.shortcuts import render

# Create your views here.
def greet(request):
    nameVar = "Deekshith"
    age = 22
    dic = {
        "name": nameVar,
        "age": age
    }
    return render(request, "index.html", dic)