from django.urls import path
from.import views
urlpatterns=[
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('contactform',views.contactform,name='contactform'),
    path('privacy',views.privacy,name='privacy'),
    path('totalitem',views.totalitem,name='totalitem'),
    path('singleitem/<int:id>/',views.singleitem,name='singleitem'),
    path('singlearea',views.singlearea,name='singlearea'),
    path('singleareadata',views.singleareadata,name='singleareadata'),
    path('signup',views.signup,name='signup'),
    path('home',views.home,name='home'),
    path('signupdata',views.signupdata, name='signupdata'),
    path('signin',views.signin,name='signin'),
    path('signindata',views.signindata,name='signindata'),
    path('logout',views.logout,name='logout'),
    path('movies',views.movies,name='movies'),
    path('tvseries',views.tvseries,name='tvseries'),
    path('music',views.music,name='music'),
    path('area',views.area,name='area'),
    path('pricing',views.pricing,name='pricing'),
    path('payment/<int:planid>/',views.payment,name='payment'),
    path('payment_success', views.payment_success, name='payment_success')

    
]