from django.shortcuts import render
from sunnyapp.models import Jobs

def index(request):
    return render(request,'Pages/index.html')

def Jobdata(request):
    #data=Jobs.objects.all()
    data=Jobs.objects.filter(loc__contains='ha')
    type='hyd'
    record={"rdata":data,"title":"Hydrabad","type":type}
    return render(request,'Pages/Viewjobs.html',record)

def Jobdata1(request):
    #data=Jobs.objects.all()
    data=Jobs.objects.filter(loc__contains='Ba')
    type="bng"
    record={"rdata":data,"title":"Banglore","type":type}
    return render(request,'Pages/banglore.html',record)  

def Jobdata2(request):
    #data=Jobs.objects.all()
    data=Jobs.objects.filter(loc__startswith='a')
    type="pune"
    record={"rdata":data,"title":"Pune","type":type}
    return render(request,'Pages/pune.html',record)     
    