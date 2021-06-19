from django.shortcuts import render,redirect, HttpResponseRedirect
from django.contrib.auth.models import User, auth

from django.contrib import messages
from .models import User


import psycopg2 as db
from django.contrib.auth import login, authenticate ,logout

from operator import itemgetter
from django.http import HttpResponse





# Create your views here.
def welcome(request):
	return render(request,'welcome.html')

def login(request):
	conn = db.psycopg2.connect(host='localhost', dbname='loginapp', user='postgres', password='1234')
	print("Database Connected....")
	cursor=conn.cursor()
	conn2 = db.psycopg2.connect(host='localhost', dbname='loginapp', user='postgres', password='1234')
	cursor2=conn2.cursor()
	sqlcommand = "select email from loginapp_user"
	sqlcommand2 = "select password from loginapp_user"
	cursor.execute(sqlcommand)
	cursor2.execute(sqlcommand2)

	e=[]
	p=[]
	for i in cursor:
		e.append(i)
	for j in cursor2:
		p.append(j)
	res = list(map(itemgetter(0),e))
	res2 = list(map(itemgetter(0),e))
	print(res)
	if request.method=="POST":
		email = request.POST['email']
		password = request.POST['password']
		i = 1
		k = len(res)
		while i < k:
			if res[i]==email and res2[i]==password:
				return render(request,'welcome.html',{'email':email})
				

				break
			i+=1
		else:
			messages.info(request,"check Username and password")
			return redirect('dashboard')
	return render(request,'loginapp/login.html')

def register(request):

	if request.method == 'POST':
		user = User()

		user.username = request.POST.get('username')
		user.email = request.POST.get('email')
		user.password = request.POST.get('password')
		user.repassword = request.POST.get('repassword')
		user.address = request.POST.get('address')
		

		user.save()
			



		if user.password!=user.repassword:
			messages.info(request,'password not matching...')
			return redirect('register')
		
		else:
			return redirect('login')

			#user.username==user.email or user.password==user.username:
			#messages.info(request,'user has been created')
			#return redirect('register')	
		#elif user.username =="" or user.password =="":
			#messages.info(request,'some field is missing')
			#return redirect('register')
	
	return render(request,"register.html" )

def dashboard(request):
	context = {'dashboard':User.objects.all()}

	return render(request,'loginapp/dashboard.html',context)



def user_delete(request, id):
	if request.method == 'POST':
		pi = User.objects.get(pk=id)
		pi.delete()
		messages.info(request,'user has been deleted')
	return HttpResponseRedirect('/')
def update_data(request, id):
	user = User.objects.get(id = id)	
	return render(request,'update_data.html',{'user':user})

def edit(request, id):
	user = User(id=id)

	user.username = request.GET['username']
	user.email = request.GET['email']
	user.password = request.GET['password']
	user.repassword = request.GET['repassword']
	user.address = request.GET['address']
	import datetime	
	updated_at = datetime.datetime.now()
	user.created_at = updated_at
	user.save()
	context = {'edit':User.objects.all()}
	return render(request,'loginapp/login.html',context)


	
	

def logout(request):
	messages.info(request,'You have successfully logout...!')
	return HttpResponseRedirect('/')


	
