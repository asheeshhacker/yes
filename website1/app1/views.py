from django.shortcuts import render
from .models import data1

# Create your views here.
def index(request):
    data2 = data1.objects.get(id=1)
    print(data2.pic.url)
    return render(request,'index.html',{'data1':data2})