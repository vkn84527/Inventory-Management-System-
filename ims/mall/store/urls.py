from django.conf.urls import url,include
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index,name="index"), 
    url(r'^clothes/', views.clothes,name="clothes"), 
    url(r'^login/', views.login,name="login"), 
    url(r'^register/', views.register,name="register"),
    url(r'^doregister/', views.doregister,name="doregister"),
    url(r'^dologin/', views.dologin,name="dologin"), 
    url(r'^logout/', views.logout,name="logout"), 
    url(r'^checkout/', views.checkout,name="checkout"), 
    url(r'^contact/', views.contact,name="contact"), 
    url(r'^mobile/', views.mobile,name="mobile"), 
    url(r'^email/', views.email,name="email"), 
    url(r'^fruits/', views.fruits,name="fruits"), 
    url(r'^watch/', views.watch,name="watch"), 
    url(r'^phone/', views.phone,name="phone"), 
    url(r'^term/', views.term,name="term"), 
    

]
