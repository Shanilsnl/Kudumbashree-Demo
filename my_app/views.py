from django.shortcuts import render
from my_app.models import *
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from django.contrib.auth import logout
def first(request):
	return render(request,'home/index.html')
def contact(request):
	return render(request,'home/contact.html')
def about(request):
	return render(request,'home/about.html')
def login(request):
	if request.method=='POST':
		email=request.POST['email']
		password=request.POST['password']
		d=reg.objects.all().filter(email=email,password=password)
		if d:
			for x in d:
				request.session['loginid']=x.id
				c=x.usertype
				if c=='admin':
					return HttpResponseRedirect('/adm/')
				elif c=='president':
					return HttpResponseRedirect('/president/')
				else:
					return HttpResponseRedirect('/secretary/')
		else:	
	
			return render(request,'home/login.html',{'msg':'does not exist'})
	return render(request,'home/login.html')
def adm(request):
	if request.session.has_key('loginid'):
		return render(request,'admin/index.html')
	else:
		return render(request,'home/login.html')
def president(request):
	return render(request,'president/index.html')
def secretary(request):
	return render(request,'secretary/index.html')
def addm(request):
	if request.session.has_key('loginid'):
		if request.method=='POST':
			name=request.POST['name']
			email=request.POST['email']
			phone=request.POST['phone']
			age=request.POST['age']
			aadhar=request.POST['aadhar']
			status=request.POST['status']
			address=request.POST['address']
			if mem.objects.all().filter(email=email):
				return render(request,'admin/add_members.html',{'msg':'same email already exist'})
			else:
				a=mem(name=name,email=email,phone=phone,age=age,aadhar=aadhar,status=status,address=address)
				a.save()
		return render(request,'admin/add_members.html')
	else:
		return render(request,'home/login.html')
def pro(request):
	a=request.GET["p"]
	ab="null"
	b=mem.objects.filter(email=a)
	if b:
		dat={'aa':ab}
		return JsonResponse(dat)
	else:
		c=''
		dat={'aa':c}	
		return JsonResponse(dat)

def log(request):
	if request.session.has_key('loginid'):
		del request.session['loginid']
	logout(request)
	return render(request,'home/login.html')
import datetime
from django.db.models import Q
def attndc(request):
	if request.session.has_key('loginid'):
		a=datetime.datetime.now()
		d=a.strftime('%x')
		t=a.strftime('%X')
		if request.method=='POST':
			a1=request.POST['att']
			a2=mem.objects.get(id=a1)
			if att.objects.filter(rg1=a1,date=d):
				return HttpResponseRedirect('/attndc/')
			else:
				a3=att(rg1=a2,date=d,time=t)
				a3.save()
				return HttpResponseRedirect('/attndc/')
		else:
			c=att.objects.filter(date=d)
			c1=[]
			for x in c:
				c1.append(x.rg1.id)
			c2=mem.objects.filter(~Q(id__in=c1))
			print(c2)
			#m3=att.objects.all().filter(date=d)
			a1=att.objects.values_list('date',flat=True).distinct()
			return render(request,'admin/attendence.html',{'b':c2,'c':a1,})

	else:
		return render(request,'home/login.html')
#def v_attndc(request):
	#if request.session.has_key('loginid'):
		#a=att.objects.all()
		#return render(request,'admin/v_att.html',{'b':a})
def loanapp(request):
	if request.session.has_key('loginid'):
		a=mem.objects.all()
		return render(request,'admin/loan_app.html',{'b':a})
	else:
		return render(request,'home/login.html')
def pro_ajax(request):
	we=request.GET["p"]
	print(we)
	var=mem.objects.all().filter(id=we)
	for x in var:
		d1=x.name
		d2=x.email
		d3=x.phone
		d4=x.age
		d5=x.status

		print(d3)
		dat={"aa":d1,'bb':d2,'cc':d3,'dd':d4,'ee':d5}
	return JsonResponse(dat)
def loannn(request):
	if request.session.has_key('loginid'):
		if request.method=='POST':
			c=request.POST['aadhar']
			d=request.POST['income']
			e=request.POST['loan_type']
			status=request.POST['status']
			f=request.POST['amount']
			h=mem.objects.get(id=c)
			g=int(f)+int(f)*0.1

			c_list=['Active','Approved']
			if loan.objects.filter(rg1=c,status__in=c_list):
				a=mem.objects.all()
				return render(request,'admin/loan_app.html',{'msg':'A loan is currently active','b':a})


			else:
				a=loan(rg1=h,income=d,loan_type=e,amount=f,status='Active',b_amount=int(g))
				a.save()
				return render(request,'admin/loan_app.html')
	else:
		return render(request,'home/login.html')
def loan_appr(request):
	if request.session.has_key('loginid'):
		a=loan.objects.filter(status='Active')
		return render(request,'admin/loan_appr.html',{'b':a})
	else:
		return render(request,'home/login.html')
def appr(request):
	if request.session.has_key('loginid'):
		a=request.GET['a']
		b=loan.objects.filter(id=a).update(status='Approved')
		a=loan.objects.all().filter(status='Active')
		return render(request,'admin/loan_appr.html',{'b':a})
	else:
		return render(request,'home/login.html')
def loan_tr(request):
	if request.session.has_key('loginid'):
		a=loan.objects.filter(status='Approved')
		return render(request,'admin/loan_tr.html',{'b':a})
	else:
		return render(request,'home/login.html')
def add_amount(request):
	if request.session.has_key('loginid'):
		if request.method=='GET':
			a=request.GET['a']
			b=loan.objects.filter(id=a)
		return render(request,'admin/add_amount.html',{'b':b})
	else:
		return render(request,'home/login.html')
def rep(request):
	if request.session.has_key('loginid'):
		e=datetime.datetime.now()
		d=e.strftime('%x')
		t=e.strftime('%X')
		if request.method=='POST':
			cd=request.POST['pd']
			ed=request.POST['r_amount']
			fd=loan.objects.get(id=cd)
			ba=request.POST['bl']
			bal=float(ba)-float(ed)
			if bal<0:
				ef=loan.objects.filter(id=cd)
				return render(request,'admin/add_amount.html',{'b':ef,'msg':'Repay amount is greater than balance amount..!!'})
			else:
				dt=repay(rg1=fd,r_amount=ed,date=d,time=t)
				dt.save()
				ba2=loan.objects.filter(id=cd).update(b_amount=int(bal))
				if bal==0:
					c=loan.objects.filter(id=cd).update(status='Closed')
					a=loan.objects.filter(status='Approved')
					return render(request,'admin/loan_tr.html',{'b':a})
				return HttpResponseRedirect('/loan_tr/')
	else:
		return render(request,'home/login.html')
def loan_st(request):
	if request.session.has_key('loginid'):
		a=loan.objects.filter(status='Approved')
		return render(request,'admin/loan_status.html',{'b':a})
	else:
		return render(request,'home/login.html')
def loan_his(request):
	if request.session.has_key('loginid'):
		if request.method=='POST':
			a=request.POST['att']
			if a=='null':
				return HttpResponseRedirect('/loan_st/')
			else:	
				b=loan.objects.filter(id=a)
				c=repay.objects.filter(rg1=a)
				if c:
					return render(request,'admin/loan_history.html',{'b':b,'c':c})
				else:
					return render(request,'admin/loan_history.html',{'b':b,'c':c,'msg':'Nothing paid yet.'})
	else:
		return render(request,'home/login.html')
import json
def att_dis(request):
	we=request.GET['p']
	result_set=[]
	var=[]
	var=att.objects.all().filter(date=we)
	for x in var:
		result_set.append({'name':x.rg1.name,'date':x.date,'tim':x.time})
	return HttpResponse(json.dumps(result_set),content_type='application/json')
def admp(request):
	if request.session.has_key('loginid'):
		return render(request,'president/index.html')
	else:
		return render(request,'home/login.html')	
def addmp(request):
	if request.session.has_key('loginid'):
		if request.method=='POST':
			name=request.POST['name']
			email=request.POST['email']
			phone=request.POST['phone']
			age=request.POST['age']
			aadhar=request.POST['aadhar']
			status=request.POST['status']
			address=request.POST['address']
			if mem.objects.all().filter(email=email):
				return render(request,'president/add_membersp.html',{'msg':'same email already exist'})
			else:
				a=mem(name=name,email=email,phone=phone,age=age,aadhar=aadhar,status=status,address=address)
				a.save()
		return render(request,'president/add_membersp.html')
	else:
		return render(request,'home/login.html')
def loan_apprp(request):
	if request.session.has_key('loginid'):
		a=loan.objects.filter(status='Active')
		return render(request,'president/loan_apprp.html',{'b':a})
	else:
		return render(request,'home/login.html')
def attndcp(request):
	if request.session.has_key('loginid'):
		a=datetime.datetime.now()
		d=a.strftime('%x')
		t=a.strftime('%X')
		c=att.objects.filter(date=d)
		c1=[]
		for x in c:
			c1.append(x.rg1.id)
		c2=mem.objects.filter(~Q(id__in=c1))
		print(c2)
		#m3=att.objects.all().filter(date=d)
		a1=att.objects.values_list('date',flat=True).distinct()
		return render(request,'president/attendencep.html',{'b':c2,'c':a1})

	else:
		return render(request,'home/login.html')
def loan_stp(request):
	if request.session.has_key('loginid'):
		a=loan.objects.filter(status='Approved')
		return render(request,'president/loan_statusp.html',{'b':a})
	else:
		return render(request,'home/login.html')
def loan_hisp(request):
	if request.session.has_key('loginid'):
		if request.method=='GET':
			a=request.GET['a']
			if a=='null':
				return HttpResponseRedirect('/loan_stp/')
			else:
				b=loan.objects.filter(id=a)
				c=repay.objects.filter(rg1=a)
				if c:
					return render(request,'president/loan_historyp.html',{'b':b,'c':c})
				else:
					return render(request,'president/loan_historyp.html',{'b':b,'c':c,'msg':'Nothing paid yet.'})

	else:
		return render(request,'home/login.html')
def apprp(request):
	if request.session.has_key('loginid'):
		a=request.GET['a']
		b=loan.objects.filter(id=a).update(status='Approved')
		a=loan.objects.all().filter(status='Active')
		return render(request,'president/loan_apprp.html',{'b':a})
	else:
		return render(request,'home/login.html')
def adms(request):
	if request.session.has_key('loginid'):
		return render(request,'secretary/index.html')
	else:
		return render(request,'home/login.html')
def addms(request):
	if request.session.has_key('loginid'):
		if request.method=='POST':
			name=request.POST['name']
			email=request.POST['email']
			phone=request.POST['phone']
			age=request.POST['age']
			aadhar=request.POST['aadhar']
			status=request.POST['status']
			address=request.POST['address']
			if mem.objects.all().filter(email=email):
				return render(request,'secretary/add_memberss.html',{'msg':'same email already exist'})
			else:
				a=mem(name=name,email=email,phone=phone,age=age,aadhar=aadhar,status=status,address=address)
				a.save()
		return render(request,'secretary/add_memberss.html')
	else:
		return render(request,'home/login.html')
def attndcs(request):
	if request.session.has_key('loginid'):
		a=datetime.datetime.now()
		d=a.strftime('%x')
		t=a.strftime('%X')
		if request.method=='POST':
			a1=request.POST['att']
			a2=mem.objects.get(id=a1)
			a3=att(rg1=a2,date=d,time=t)
			a3.save()
			return HttpResponseRedirect('/attndcs/')
		else:
			c=att.objects.filter(date=d)
			c1=[]
			for x in c:
				c1.append(x.rg1.id)
			c2=mem.objects.filter(~Q(id__in=c1))
			print(c2)
			#m3=att.objects.all().filter(date=d)
			a1=att.objects.values_list('date',flat=True).distinct()
			return render(request,'secretary/attendence_marking.html',{'b':c2,'c':a1,})

	else:
		return render(request,'home/login.html')
def loanapps(request):
	if request.session.has_key('loginid'):
		a=mem.objects.all()
		return render(request,'secretary/loan_apps.html',{'b':a})
	else:
		return render(request,'home/login.html')
def loannns(request):
	if request.session.has_key('loginid'):
		if request.method=='POST':
			c=request.POST['aadhar']
			d=request.POST['income']
			e=request.POST['loan_type']
			status=request.POST['status']
			f=request.POST['amount']
			h=mem.objects.get(id=c)
			g=int(f)+int(f)*0.1

			if loan.objects.filter(rg1=c,status='Active'):
				a=mem.objects.all()
				return render(request,'secretary/loan_apps.html',{'msg':'A loan is currently active','b':a})


			else:
				a=loan(rg1=h,income=d,loan_type=e,amount=f,status='Active',b_amount=int(g))
				a.save()
				return render(request,'secretary/loan_apps.html')
	else:
		return render(request,'home/login.html')
def loan_trs(request):
	if request.session.has_key('loginid'):
		a=loan.objects.filter(status='Approved')
		return render(request,'secretary/loan_trs.html',{'b':a})
	else:
		return render(request,'home/login.html')
def add_amounts(request):
	if request.session.has_key('loginid'):
		if request.method=='GET':
			a=request.GET['a']
			b=loan.objects.filter(id=a)
		return render(request,'secretary/add_amounts.html',{'b':b})
	else:
		return render(request,'home/login.html')
def reps(request):
	if request.session.has_key('loginid'):
		e=datetime.datetime.now()
		d=e.strftime('%x')
		t=e.strftime('%X')
		if request.method=='POST':
			cd=request.POST['pd']
			ed=request.POST['r_amount']
			fd=loan.objects.get(id=cd)
			ba=request.POST['bl']
			bal=float(ba)-float(ed)
			if bal<0:
				ef=loan.objects.filter(id=cd)
				return render(request,'admin/add_amount.html',{'b':ef,'msg':'Repay amount is greater than balance amount..!!'})
			else:
				dt=repay(rg1=fd,r_amount=ed,date=d,time=t)
				dt.save()
				ba2=loan.objects.filter(id=cd).update(b_amount=int(bal))
				if bal==0:
					c=loan.objects.filter(id=cd).update(status='Closed')
					a=loan.objects.filter(status='Approved')
					return render(request,'admin/loan_tr.html',{'b':a})
				return HttpResponseRedirect('/loan_tr/')
	else:
		return render(request,'home/login.html') 

	













#def pay(request):
	#if request.session.has_key('loginid'):
		#a=request.GET['a']
		#b=loan.objects.filter(id=a)
		#return render(request,'admin/add_amount.html',{'b':a})
	#else:
		#return render(request,'home/login.html')






# Create your views here.
