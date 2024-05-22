from django.shortcuts import render
def home(request):
    return render(request,'app4/index.html',{'param1':"hello"})
# Create your views here.
