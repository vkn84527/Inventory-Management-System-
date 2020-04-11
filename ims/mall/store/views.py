from django.shortcuts import render
from .models import User
from .models import Product
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password


# Create your views here.

def index(request):
	if request.session.has_key('user'):
		
		status = False
		return render(request,"index.html",{'logstatus':status,'name':request.session['name']})
		
	else:
		status = True
		return render(request,"index.html",{'logstatus':status})


def clothes(request):
	if request.session.has_key('user'):
		status = False
		return render(request,"clothes.html",{'logstatus':status,'name':request.session['name']})
	else:
		status = True
		return render(request,"clothes.html",{'logstatus':status})

def login(request):
	return render(request,"login.html")
def register(request):
	return render(request,"register.html")
def doregister(request):
	tem={'default1':False,'default2':False,}
	if request.method == "POST":
		form=User()
		
		try:
			data=User.objects.get(email=request.POST['email'])
			tem['default2']=True
			return render(request,"register.html",tem)
			
		except:
			form.name =request.POST['name']
			form.email =request.POST['email']
			form.passw =make_password(request.POST['pass'])
			form.address =request.POST['address']
			form.city =request.POST['city']
			form.state =request.POST['state']
			form.pincode =request.POST['pin']
			form.phone =request.POST['phone']
			form.dob =request.POST['dob']
			form.save()
			tem['default1']=True
			return render(request,"register.html",tem)
def dologin(request):
	data={'default1':False,'default2':False,'default3':False,}

	if request.method=="POST":
		try:
			user=User.objects.filter(email=request.POST['email']).values()[0] #dictionary
			if check_password(request.POST['pass'],user['passw']):
				#create a session variable user
				data['default1']=True
				request.session['user']=request.POST['email']
				request.session['add']=str(user['address'])
				request.session['name']=str(user['name'])
				data['name']=request.session['name']
				data['id']=request.session['user']
				return render(request,"login.html",data)
				

			else:
				data['default3']=True
				return render(request,"login.html",data)
				


		except:
			data['default2']=True
			return render(request,"login.html",data)



def logout(request):
	if request.session.has_key('user'):
		del request.session['name']
		del request.session['user']
		del request.session['add']

	return render(request,"login.html")	 

def checkout(request):
	if request.session.has_key('user'):
		return render(request,"checkout.html",{'default':True,'add':request.session['add'],'name':request.session['name']})
	else:
		return render(request,"checkout.html",{'default':False,})


def watch(request):
	return render(request,"watch.html")
def term(request):
	return render(request,"term.html")
def mobile(request):
	return render(request,"mobile.html")
def email(request):
	return render(request,"email.html")
def phone(request):
	return render(request,"phone.html")
def fruits(request):
	return render(request,"fruits.html")
def contact(request):
	return render(request,"contact.html")


		


	
        
	