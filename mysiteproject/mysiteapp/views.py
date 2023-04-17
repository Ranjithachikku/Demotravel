from django.shortcuts import render
from . models import place,person

def demo(request):
    obj=place.objects.all()
    obj1=person.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})

# Create your views here.
