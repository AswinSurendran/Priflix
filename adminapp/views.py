from django.shortcuts import render,redirect
from.models import *
from flixapp.models import Register,Contact,Singlearea

def base(request):
    data=Register.objects.all().order_by('-id')
    data1=Contact.objects.all().order_by('-id')
    data2=Categories.objects.all().order_by('-id')
    category=Categories.objects.filter(area='MOVIE').count()
    item=Categories.objects.all().count()
    comment=Contact.objects.all().count()
    review=Contact.objects.all().count()
    user=Register.objects.all().count()

    return render(request,'base.html',{'data':data,'data1':data1,'data2':data2,'category':category,'item':item,'comment':comment,'review':review,'user':user})

def catalog(request):
    return render(request,'catalog.html')

def Catalogs(request):
    if request.method=='POST':
        title=request.POST['title']
        rating=request.POST['rating']
        category=request.POST['category']
        watched=request.POST['watched']
        date=request.post['date']
        data=Catalogs(title=title,rating=rating,category=category,watched=watched,date=date)
        data.save()
        return redirect('catalog')




def additem(request):
    return render (request,'additem.html')

def  categories(request):
    if request.method=='POST':
        image=request.FILES['image']
        title=request.POST['title']
        description=request.POST['description']
        releaseyear=request.POST['releaseyear']
        runtime=request.POST['runtime']
        quality=request.POST['quality']
        country=request.POST['country']
        genre=request.POST['genre']
        area=request.POST['area']
        video=request.FILES['video']
        print(video)
        link=request.POST['link']
        data=Categories(image=image,title=title,description=description,releaseyear=releaseyear,runtime=runtime,quality=quality,country=country,genre=genre,area=area,video=video,link=link)
        data.save()
        return redirect('catalog')
    

def contacttable(request):
    data=Contact.objects.all()
    return render(request,'contacttable.html',{'data':data})

def registable(request):
    data=Register.objects.all()
    return render(request,'registable.html',{'data':data})  

def pricetable(request):
    data=SubscriptionPlan.objects.all()
    return render(request,'pricetable.html',{'data':data}) 
def price(request):
    return render(request,'price.html')
def pricedata(request):
    if request.method=='POST':
        name=request.POST['name']
        price=request.POST['price']
        validity=request.POST['validity']
        features=request.POST['features']
        data=SubscriptionPlan(name=name,price=price,validity=validity,features=features)
        data.save()
    return redirect('pricetable')    




    


# Create your views here.
