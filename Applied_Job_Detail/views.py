from django.shortcuts import render,redirect
from .models import userlogin,company_detail,profile,todolist
from django.conf import settings
from django.core.mail import send_mail
import random
# Create your views here.
def home(request):
	if request.session.get('user'):
		return redirect("dashboard")
	if request.session.get('error'):
		error=request.session.get('error')
		del request.session['error']
		return render(request,'index.html',{'error':error})
	else:
		return render(request,'index.html')
def authenticate(request):
	user=request.POST['user']
	password=request.POST['pass']
	res=userlogin.objects.filter(username=user,password=password)
	if len(res)==1:
		request.session['user']=res[0].username
		return redirect("dashboard")
	else:
		request.session['error']="Username or Password is incorrect."
		return redirect('home')
def dashboard(request):
	if request.session.get('user') and request.session.get('error'):
		res=request.session.get('user')
		error=request.session.get('error')
		del request.session['error']
		re="amitv25047@gmail.com"
		return render(request,"dashboard.html",{'res':res,'re':re,'error':error})
	if request.session.get('user'):
		res=request.session.get('user')
		re="amitv25047@gmail.com"
		return render(request,"dashboard.html",{'res':res,'re':re})
	else:
		return redirect("home")
def logout(request):
	if request.session.get('user'):
		del request.session['user']
		return redirect("home")
def change_Password(request):
	if request.session.get('user'):
		return render(request,'change password.html')
	else:
		return redirect('home')
def add(request):
	if request.session.get('user'):
		user=request.session.get('user')
		return render(request,'Add_company_detail.html',{'res':user})
	else:
		return redirect('home')
def Add_detail(request):
	if request.session.get('user'):
		user=request.session.get('user')
		company=request.POST['company']
		position=request.POST['position']
		ctc=request.POST['ctc']
		date=request.POST['date']
		email=request.POST['email']
		mobile=request.POST['mobile']
		status=request.POST['status']
		company=company.upper()
		jobid=random.randint(1000000, 2000000)
		r=company_detail.objects.filter(jobid=jobid,username=user)
		while(len(r)==1):
			jobid=random.randint(1000000, 2000000)
			r=company_detail.objects.filter(jobid=jobid,username=user)
		res=company_detail.objects.filter(username=user,compnay_name=company,position=position,ctc=ctc)
		if len(res)>=1:
			return render(request,'Add_company_detail.html',{'error':'Company Profile applied detail Already Exist'})
		if len(res)==0:
			res=company_detail(jobid=jobid,username=user,compnay_name=company,ctc=ctc,position=position,date=date,email=email,mobile=mobile,status=status)
			res.save()
			return render(request,'Add_company_detail.html',{'error':'Company Profile applied detail Saved Successfully'})
	else:
		return redirect('home')
def companies(request):
	if request.session.get('user'):
		username=request.session.get('user')
		res=company_detail.objects.filter(username=username)
		return render(request,'company.html',{'res':res})
	else:
		return redirect('home')
def viewdetail(request):
	if request.session.get('user'):
		jobid=request.GET['d']
		res=company_detail.objects.filter(jobid=jobid)
		return render(request,'viewdetail.html',{'res':res,'jobid':jobid})
	else:
		return redirect('home')
def changestatus(request):
	if request.session.get('user'):
		jobid=request.GET['d']
		user=request.session.get('user')
		request.session['jobid']=jobid
		res=company_detail.objects.filter(jobid=jobid,username=user)
		return render(request,'changestatus.html',{'res':res,'jobid':jobid})
	else:
		return redirect('home')

def updates(request):
	if request.session.get('user'):
		user=request.session.get('user')
		jobid=request.session.get('jobid')
		status=request.POST['status']
		'''company=request.POST['company']
		jobid=request.POST['jobid']
		position=request.POST['position']
		ctc=request.POST['ctc']
		date=request.POST['date']
		email=request.POST['email']
		mobile=request.POST['mobile']
		status=request.POST['status']
		user=request.session.get('user')
		res=company_detail(jobid=jobid,username=user,compnay_name=company,ctc=ctc,position=position,date=date,email=email,mobile=mobile,status=status)
		res.save()'''
		res=company_detail.objects.get(username=user,jobid=jobid)
		res.status=status
		res.save()
		del request.session['jobid']
		request.session['error']="Job Status Updated Successfully."
		return redirect('dashboard')
	else:
		return redirect('home')

def changedetail(request):
	if request.session.get('user'):
		jobid=request.GET['d']
		user=request.session.get('user')
		request.session['jobid']=jobid
		res=company_detail.objects.filter(jobid=jobid,username=user)
		return render(request,'changedetail.html',{'res':res,'jobid':jobid})
	else:
		return redirect('home')

def updatedetail(request):
	if request.session.get('user'):
		user=request.session.get('user')
		jobid=request.session.get('jobid')
		company=request.POST['company']
		company=company.upper()
		position=request.POST['position']
		ctc=request.POST['ctc']
		date=request.POST['date']
		email=request.POST['email']
		mobile=request.POST['mobile']
		re=company_detail.objects.get(username=user,jobid=jobid)
		status=re.status
		user=request.session.get('user')
		res=company_detail(jobid=jobid,username=user,compnay_name=company,ctc=ctc,position=position,date=date,email=email,mobile=mobile,status=status)
		res.save()
		del request.session['jobid']
		request.session['error']="Company Detail Updated Successfully."
		return redirect('dashboard')
	else:
		return redirect('home')
def companysearch(request):
	if request.session.get('user'):
		username=request.session.get('user')
		company=request.POST['search']
		company=company.upper()
		res=company_detail.objects.filter(username=username,compnay_name=company)
		if len(res)>0:
			return render(request,'company.html',{'res':res})
		else:
			return render(request,'company.html',{'res':res})

	else:
		return redirect('home')
def create_user_account(request):
	if request.session.get('user'):
		return render(request,"create_profile.html")
	else:
		return redirect('home')
def created(request):
	if request.session.get('user'):
		auser=request.POST['email']
		if len(userlogin.objects.filter(username=auser))==0:
			mobile=request.POST['mobile']
			name=request.POST['name']
			dob=request.POST['dob']
			password=random.randint(1000000, 2000000)
			q = profile(username=auser, name=name, mobile=mobile, dob=dob)
			q.save()
			q=userlogin(username=auser,password=password)
			q.save()
			subject = 'Welcome|Login Created Successfully'
			message = f'Hi {name},\nYour login Account has been Created Successfully. Check below login Details-\nUsername : {auser} \nPaswword : {password}.\nPlease change your password in First Login.\n\n\nThank You\nAdmin\n(Personal)\n\n\nImportant Note: Please do not share your Personal password  with anyone.'
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [auser ]
			send_mail( subject, message, email_from, recipient_list )
			request.session['error']="Profile Created Successfully"
			return redirect('dashboard')
		else:
			return render(request,"create_profile.html",{'error':"Email is already exist"})
	else:
		return redirect('home')
def myprofile(request):
	if request.session.get('user'):
		auser=request.session.get('user')
		res=profile.objects.filter(username=auser)
		if len(res)==0:
			res=request.session.get('user')
			return render(request,'myprofile.html',{'res':res})
		if len(res)==1:
			return render(request, 'myprofile.html', {'res': res})
	else:
		return redirect('home')
def update(request):
	if request.session.get('user'):
		auser=request.session.get('user')
		name=request.POST['name']
		mobile=request.POST['mobile']
		dob=request.POST['dob']
		res=profile.objects.filter(username=auser)
		if len(res)==1:
			q = profile(username=auser, name=name, mobile=mobile, dob=dob)
			q.save()
			res = profile.objects.filter(username=auser)
			return render(request, 'myprofile.html', {'res':res,'error':'Profile Updated Successfully.'})
	else:
		return redirect('home')
def change(request):
	if request.session.get('user'):
		auser=request.session.get('user')
		old=request.POST['old']
		apass=request.POST['new1']
		apass1=request.POST['new2']
		res = userlogin.objects.filter(username=auser,password=old)
		if len(res)==1:
			if apass==apass1:
				k=userlogin.objects.get(username=auser,password=old)
				k.password = apass
				k.save()
				return render(request,'dashboard.html',{'error':'Password Updated Successfully.'})
			else:
				return render(request, 'change password.html', {'error': 'Password and Re-enter password should be same.'})

		else:
			return render(request,'change password.html',{'error':'Old Password is incorrect.'})
	else:
		return redirect('home')
def users(request):
	if request.session.get('user'):
		auser=request.session.get('user')
		if request.session.get('error'):
			error=request.session.get('error')
			del request.session['error']
		else:
			error=""
		res=profile.objects.exclude(username=auser).order_by('name')
		return render(request,'user_profiles.html',{'res':res,'error':error})
def deleteuseraccount(request):
	if request.session.get('user'):
		auser=request.GET['d']
		res=profile.objects.get(username=auser)
		subject = 'Thank you|Login Deleted'
		message = f'Hi {res.name},\nThank you for taking my services.Your account has been deleted successfully.Good luck for Your Future.\n\n\nThank You\nAdmin(Personal)'
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [auser ]
		send_mail( subject, message, email_from, recipient_list )
		profile.objects.filter(username=auser).delete()
		userlogin.objects.filter(username=auser).delete()
		request.session['error']="User Profile Deleted Successfully"
		return redirect('users')
	else:
		return redirect('home')
def getpassword(request):
	if request.session.get('user'):
		auser=request.session.get('user')
		res=userlogin.objects.exclude(username=auser).order_by('username')
		return render(request,'user_login_detail.html',{'res':res})
	else:
		return redirect('home')


		

def datesearch(request):
	if request.session.get('user'):
		username=request.session.get('user')
		date=request.POST['search']
		res=company_detail.objects.filter(username=username,date=date)
		if len(res)>0:
			return render(request,'company.html',{'res':res})
		else:
			return render(request,'company.html',{'res':res})

	else:
		return redirect('home')

def sortcompany(request):
	if request.session.get('user'):
		res=company_detail.objects.filter(username=request.session.get('user')).order_by('compnay_name')
		return render(request,'company.html',{'res':res})
	else:
		return redirect('home')
def sortdate(request):
	if request.session.get('user'):
		res=company_detail.objects.filter(username=request.session.get('user')).order_by('-date')
		return render(request,'company.html',{'res':res})
	else:
		return redirect('home')
def sortctc(request):
	if request.session.get('user'):
		res=company_detail.objects.filter(username=request.session.get('user')).order_by('ctc')
		return render(request,'company.html',{'res':res})
	else:
		return redirect('home')
def sortjobid(request):
	if request.session.get('user'):
		res=company_detail.objects.filter(username=request.session.get('user')).order_by('jobid')
		return render(request,'company.html',{'res':res})
	else:
		return redirect('home')

def forget_password(request):
	return render(request,"forget_password.html")
def check_detail(request):
	auser = request.POST['auser']
	name = request.POST['name']
	mobile = request.POST['mobile']
	dob = request.POST['dob']
	res=profile.objects.filter(username=auser,name=name,mobile=mobile,dob=dob)
	if len(res)==1:
		otp=random.randint(100000, 999999)
		request.session['OTP']=otp
		subject = 'Forget Password|OTP'
		message = f'Hii {name},\nYou are Requested to Forget your Password.\nOTP-{otp}\nIf you are not requested to forget password please ignore this email.\n\n\nThank You\nAdmin\n(Personal).\n\n\nImportant Note: Please do not share your OTP with anyone.'
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [auser]
		send_mail( subject, message, email_from, recipient_list )
		return render(request,"authenticate.html",{"auser":auser,'error':"OTP sent Successfully."})
	else:
		return render(request,'forget_password.html',{"error":"Invalid User detail"})
def confirm_pass(request):
	auser = request.POST['auser']
	apass = request.POST['apass']
	againpass = request.POST['againpass']
	if apass==againpass:
		res=profile.objects.get(username=auser)
		subject = 'Password Updated'
		message = f'Hii {res.name},\nYour paswword has been changed successfully.\n\n\nThank You\nAdmin\n(Personal)'
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [auser]
		send_mail( subject, message, email_from, recipient_list )
		del request.session['OTP']
		if len(userlogin.objects.filter(username=auser))==1:
			k = userlogin.objects.get(username=auser)
			k.password = apass
			k.save()
			return render(request,"forget_password.html",{'error':"Password updated Successfully"})
	else:
		return render(request, "update_password.html", {"auser": auser,'error':"Password and Confirm Password should be same"})

def authenticates(request):
	auser=request.POST['auser']
	otp=request.POST['otp']
	otp1=request.session.get('OTP')
	if str(otp)==str(otp1):
		return render(request,'update_password.html',{'auser':auser})
	else:
		return render(request,'authenticate.html',{'auser':auser,'error':"Invalid OTP"})
def otherusers(request):
	if request.session.get('user'):
		res=company_detail.objects.exclude(username=request.session.get('user')).order_by('compnay_name')
		return render(request,'otherusercompany.html',{'res':res})
	else:
		return redirect('home')

def sortcompany1(request):
	if request.session.get('user'):
		res=company_detail.objects.exclude(username=request.session.get('user')).order_by('compnay_name')
		return render(request,'otherusercompany.html',{'res':res})
	else:
		return redirect('home')
def sortdate1(request):
	if request.session.get('user'):
		res=company_detail.objects.exclude(username=request.session.get('user')).order_by('-date')
		return render(request,'otherusercompany.html',{'res':res})
	else:
		return redirect('home')
def sortctc1(request):
	if request.session.get('user'):
		res=company_detail.objects.exclude(username=request.session.get('user')).order_by('ctc')
		return render(request,'otherusercompany.html',{'res':res})
	else:
		return redirect('home')
def sortjobid1(request):
	if request.session.get('user'):
		res=company_detail.objects.exclude(username=request.session.get('user')).order_by('jobid')
		return render(request,'otherusercompany.html',{'res':res})
	else:
		return redirect('home')
def maketodo(request):
	if request.session.get('user'):
		return render(request,'maketodolist.html')
	else:
		return redirect('home')

def Add_tododetail(request):
	if request.session.get('user'):
		topic=request.POST['topic']
		detail=request.POST['detail']
		todoid=random.randint(1000000, 2000000)
		r=todolist.objects.filter(todoid=todoid,username=request.session.get('user'))
		while(len(r)==1):
			todoid=random.randint(1000000, 2000000)
			r=todolist.objects.filter(todoid=todoid,username=request.session.get('user'))
		res=todolist(todoid=todoid,username=request.session.get('user'),topic=topic,detail=detail)
		res.save()
		return render(request,'maketodolist.html',{'error':"Item Added Successfully."})

	else:
		return redirect('home')
def viewtodo(request):
	if request.session.get('user'):
		res=todolist.objects.filter(username=request.session.get('user'))
		return render(request,'viewtodo.html',{'res':res})

	else:
		return redirect('home')
def donetodo(request):
	if request.session.get('user'):
		todoid=request.GET['d']
		todolist.objects.filter(username=request.session.get('user'),todoid=todoid).delete()
		return redirect('viewtodo')
	else:
		return redirect('home')