from django.shortcuts import render
def home(request):
    n1=5
    fact1=1
    for i in range(0,n1+1,1):
        fact1=fact1*i
    return render(request,'app2/index.html',{'param1':fact1})
# Create your views here.
