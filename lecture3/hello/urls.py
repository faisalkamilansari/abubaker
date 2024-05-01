from django.urls import path
from . import views

urlpatterns={
    path("",views.index,name="index"),
    path("name",views.showname,name="Abu"),
    #In the below code <str:name> is a variable 'name' which is passing through the views.py in function greet  
    path("<str:name>",views.greet,name="Greet"),
}