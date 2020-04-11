from django.shortcuts import render


def index(request):
	if request.session.has_key('user'):
		
		status = False
		return render(request,"index.html",{'logstatus':status,'name':request.session['name']})
	else:
		
		status = True
		return render(request,"index.html",{'logstatus':status})

