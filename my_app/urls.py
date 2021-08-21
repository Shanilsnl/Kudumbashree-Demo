from django.contrib import admin
from.import views
from django.urls import path,include

urlpatterns = [
	path('',views.first),
	path('contact/',views.contact),
	path('add_amount/',views.add_amount),
	path('about/',views.about),
	path('login/',views.login),
	path('adm/',views.adm),
	path('president/',views.president),
	path('secretary/',views.secretary),
	path('addm/',views.addm),
	path('log/',views.log),
	path('attndc/',views.attndc),
	path('loanapp/',views.loanapp),
	path('pro_ajax/',views.pro_ajax),
	path('loannn/',views.loannn),
	path('loan_appr/',views.loan_appr),
	path('approve/',views.appr),
	path('loan_tr/',views.loan_tr),
	path('add_amount/',views.add_amount),
	path('rep/',views.rep),
	path('loan_st/',views.loan_st),
	path('loan_his/',views.loan_his),
	path('att_dis/',views.att_dis),
	path('admp/',views.admp),
	path('addmp/',views.addmp),
	path('loan_apprp/',views.loan_apprp),
	path('approvep/',views.apprp),
	path('attndcp/',views.attndcp),
	path('loan_stp/',views.loan_stp),
	path('loan_hisp/',views.loan_hisp),
	path('adms/',views.adms),
	path('addms/',views.addms),
	path('attndcs/',views.attndcs),
	path('loanapps/',views.loanapps),
	path('loannns/',views.loannns),
	path('loan_trs/',views.loan_trs),
	path('reps/',views.reps),
	path('add_amounts/',views.add_amounts),
	path('pro/',views.pro),
	#path('pay/',views.pay),

	#path('v_attndc/',views.v_attndc),



]

