from django.shortcuts import render

def home(request):
    return render(request,'app1/index.html',{'param1':"Hello World"})
# Create your views here.
