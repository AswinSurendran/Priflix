from django.shortcuts import render,redirect
from adminapp.models import Categories,SubscriptionPlan, Subscribed_users
from.models import*
import datetime
import stripe
from django.conf import settings

def index(request):
    return render (request,'index.html')

def about(request):
    return render(request,'about.html')

def privacy(request):
    return render(request,'privacy.html')
def contact(request):
    return render(request,'contact.html')

def contactform(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        areas=request.POST['areas']
        comment=request.POST['comment']
        rating=request.POST['rating']
        data=Contact(name=name,email=email,subject=subject,message=message,areas=areas,comment=comment,rating=rating)
        data.save()
    return redirect('contact')
def home(request):
    return render(request,'home.html')
def totalitem(request):
    data=Categories.objects.all()
    # current_url = request.build_absolute_uri()
    # print(current_url)
    # print("---------------------------------------")
    return render (request,'totalitem.html',{'data':data})
def singleitem(request,id):
    userid=request.session.get('ui_id')
    if 'ui_id' in request.session:
        try:
            check_subscription=Subscribed_users.objects.get(user_id=userid)
            
        except Exception:
            return redirect ('pricing')
        else:
            if check_subscription.status=='ACTIVE':
                data1=Categories.objects.filter(id=id)
                return render(request,'singleitem.html',{'data1':data1})
            else:
                return redirect('pricing')           
    else:
        
        # request.session['current_path'] = 
        return render(request,'signin.html',{'msg':"you are not logined yet"})
    

def singlearea(request):
    return render(request,'singlearea.html')
def singleareadata(request):
    if request.method=='POST':
        movie=request.POST['movie']
        tvseries=request.POST['tvseries']
        music=request.POST['music']
        data=Singlearea(movie=movie,tvseries=tvseries,music=music)
        data.save()
        return redirect('singlearea')
def signup(request):
    return render(request,'signup.html')

def signupdata(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        data=Register(name=name,email=email,password=password)
        data.save()
        return redirect('signin')
    
def signin(request):
    return render(request,'signin.html')


def signindata(request):
    if request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        if Register.objects.filter(email=email,password=password).exists():
           data = Register.objects.filter(email=email,password=password).values('name','id').first()
           
           request.session['ui_id'] = data['id']
           request.session['email_u'] = email 
           request.session['username_u'] = data['name']
           request.session['password_u'] = password
           userid = request.session.get('ui_id')
           if Subscribed_users.objects.filter(user_id=userid).exists():
                subscribed_details=Subscribed_users.objects.filter(user_id=userid)
                current_date=datetime.datetime.now().date()
                expiry_date = []
                for j in subscribed_details:
                    expiry_date.append(j.expiry_date.date())
                print(current_date, expiry_date[0])
                if current_date < expiry_date[0]:
                    for i in subscribed_details:
                        i.status="INACTIVE"
                        i.save()
                else:
                    pass    
                 

           return redirect('totalitem') 
        else:
            return render(request,'signin.html',{'msg':'Invalid user credentials'})
    else:
        return redirect('signin')
def logout(request):
    
    del request.session['ui_id']
    del request.session['email_u']
    del request.session['username_u']
    del request.session['password_u']
    return redirect('totalitem')    

def movies(request):
    data1=Categories.objects.filter(area="MOVIE")
    return render(request,'totalitem.html',{'data1':data1})
def tvseries(request):
    data1=Categories.objects.filter(area="TVSERIES")
    return render(request,'totalitem.html',{'data1':data1})
def music(request):
    data1=Categories.objects.filter(area="music")
    return render(request,'totalitem.html',{'data1':data1})

def area(request):
    return render(request,'area.html')

def pricing(request):
    data=SubscriptionPlan.objects.filter()
    current_date = datetime.datetime.now()
    final_data = []
    for i in data:
        expiry_date = current_date + datetime.timedelta(days=i.validity)
        final_data.append((i, expiry_date))
    return render(request,'pricing.html',{'data':data, 'final_data':final_data})

stripe.api_key=settings.STRIPE_SECRET_KEY
def payment(request,planid):
    plan_details=SubscriptionPlan.objects.get(id=planid)

    session = stripe.checkout.Session.create(
        payment_method_types = ['card'],
        line_items=[{
                'price_data':{
                    'currency': 'inr',
                    'product_data':{
                        'name': plan_details.name,
                    },
                    'unit_amount':int(plan_details.price)*100,
                   
                },
                'quantity':1,
        }],
        mode='payment',
        success_url = "http://127.0.0.1:8000/flixapppayment_success?session_id={CHECKOUT_SESSION_ID}",
        cancel_url = "http://127.0.0.1:8000/pay_cancel",
        client_reference_id=planid,
    )
    return redirect(session.url, code=303)

    
def payment_success(request):
    user_id = request.session.get('ui_id')
    session = stripe.checkout.Session.retrieve(request.GET['session_id'])
    plan_id = session.client_reference_id
    plan_details=SubscriptionPlan.objects.get(id=plan_id)
    validity = plan_details.validity
    current_date=datetime.datetime.now()
    expiry_date=current_date + datetime.timedelta(days=validity)
    
    

    Subscribed_users.objects.create(
        user_id = Register.objects.get(id=user_id),
        plan_id=SubscriptionPlan.objects.get(id=plan_id),
        status="ACTIVE",
        expiry_date=expiry_date 
        
    )

    return render(request,'payment_success.html')

# Create your views here.
