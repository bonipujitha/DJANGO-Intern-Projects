from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
	return render(request, 'index.html')

def contact(request):
	return render(request, 'contact.html')


def facultylogindef(request):
	s='FACULTY'
	return render(request, 'faculty.html', {'s':s})

def floginaction(request):
	e=request.POST['email']
	p=request.POST['pwd']

	print(e,p,'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
	d = faculty.objects.filter(email__exact=e).filter(pwd__exact=p).count()
	if d>0:
		request.session['femail'] = e
		return render(request, 'facultyhome.html')
	else:
		return render(request, 'faculty.html',{'msg':'Login Fail'})		


	#

def fsignupaction(request):
	if request.method=='GET':
		return render(request, 'facultysignup.html')
	else:
		name=request.POST["name"]
		email=request.POST["email"]
		pwd=request.POST["pwd"]
		ph=request.POST["ph"]
		addr=request.POST["addr"]
		qua=request.POST["qua"]
		print(email)

		d=faculty(name=name, email=email, pwd=pwd, phone=ph, addr=addr, qualification=qua)
		d.save()

		return render(request, 'faculty.html',{'msg':'Account is created, you can login !!'})




def fviewprofile(request):
	if "femail" in request.session:
		e=request.session['femail']
		d=faculty.objects.filter(email__exact=e)
		return render(request, 'fviewprofile.html',{'data':d})
	else:
		return render(request, 'faculty.html',{'msg':'Session is expired, you can login !!'})



def fupdateprofile(request):
	e=request.session['femail']
	d=faculty.objects.filter(email__exact=e)
	return render(request, 'fupdateprofile.html',{'data':d})




def fupdateaction(request):
	if "femail" in request.session:
		name=request.POST["name"]
		email=request.session["femail"]
		ph=request.POST["ph"]
		addr=request.POST["addr"]
		qua=request.POST["qua"]
		
		faculty.objects.filter(email = email).update(name = name, phone = ph, addr=addr, qualification=qua)
		
		return redirect('fviewprofile')
	else:
		return render(request, 'faculty.html',{'msg':'Session is expired, you can login !!'})



def fachome(request):
	if "femail" in request.session:
		return render(request, 'facultyhome.html') 
	else:
		return render(request, 'faculty.html',{'msg':'Session is expired, you can login !!'})


def faclogout(request):
	if "femail" in request.session:
		del request.session['femail']
		return render(request, 'faculty.html') 
	else:
		return render(request, 'faculty.html',{'msg':'Session is expired, you can login !!'})

