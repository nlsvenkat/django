from django.urls import path
from . import views

urlpatterns = [
    path("form",views.add, name="add"),
    path("result",views.result,name="result"),
    
    path("quiz",views.quiz,name="quiz")
]