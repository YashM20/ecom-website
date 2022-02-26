from django.shortcuts import render, redirect
from .models import Company_data
from django.http import HttpResponse

import smtplib
import random
import email.message
 
def Company_login(request):
    if request.POST:
        em = request.POST['email']
        ps = request.POST['pass']
        
        try:
            var = Company_data.objects.get(com_em = em)
            print(var)
            if var.com_pass == ps:
                request.session['comp_data'] = var.id
                return redirect('Dashboard')
            else:
                return HttpResponse("<h2><a href="">Wrong Password..!</a></h2>")   
        except:
            return HttpResponse("<h2><a href="">Wrong Email or Password..! </a></h2>")

    return render(request,'company/login/login.html')

def Company_register(request):
    if request.POST:
        nm = request.POST['name']
        em = request.POST['email']
        pass1 = request.POST['pass']
        pass2 = request.POST['re_pass']

        try:
            var = Company_data.objects.get(com_em = em)
            return HttpResponse("<h2><a href="">Email already Registered..! </a></h2>")
        except:
            if pass1 == pass2:
                obj = Company_data()
                obj.com_name = nm
                obj.com_em = em
                obj.com_pass = pass2
                obj.save()
                return redirect('c_login')
            else:
                return HttpResponse("<h2><a href="">Email already Registered..! </a></h2>")

    return render(request,'company/login/register.html')

 

  
def New_pass(request):
    if 'new_user' in request.session.keys():
        if request.POST:
            p1 = request.POST['pass1']
            p2 = request.POST['pass2']
            print(p1,p2)
            if p1 == p2:
                obj = Company_data.objects.get(id = int(request.session['new_user']))
                obj.com_pass = p2 
                obj.save()
                del request.session['new_user']
                return redirect('c_login')
            else:
                return HttpResponse('<a href="">Passwords Does not match...!</a>')
        return render(request,'company/login/new_pass.html')
    else:
        return redirect('c_login')    

def Comp_forgetpass(request):
    if request.POST:
        em1 = request.POST['em']
        print(em1)
        try:
            valid = Company_data.objects.get(com_em = em1)
            print(valid)
 
            sender_email = 'royalchallenger.rc@gmail.com'
            sender_pass = '*yash20*'
            reciv_email = em1


            server = smtplib.SMTP('smtp.gmail.com',587)

            # otp=====================================================
            
            nos = [1,2,3,4,5,6,7,8,9,0]
            otp = ""
            for i in range(4):
                otp += str(random.choice(nos))
                print(otp)
            print(otp)

            mes1 = f"""
            This is your OTP
            {otp}


            Don't share it with others...
            """

            msg = email.message.Message()
            msg['Subject'] = "OTP from This Site"
            msg['From'] = sender_email
            msg['To'] = reciv_email
            password = sender_pass
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(mes1)

            server.starttls()
            server.login(msg['From'],password)
            server.sendmail(msg['From'],msg['To'],msg.as_string())

            request.session['otp'] = otp
            request.session['new_user'] = valid.id
            return redirect('OTP_check')
        except:
            return HttpResponse('<a href=""> You have Entered Wrong Email ID <a>')
    return render(request,'company/login/forget_pass.html')


def OTP_check(request):
    if 'otp' in request.session.keys():
        print("New Otp Check")
        if request.POST:
            ot1 = request.POST['ot1']
            print(ot1)
            otp = request.session['otp']
            print(otp)
            if ot1 == otp:
                del request.session['otp']
                print("Ready to create new password")
                return redirect('New_pass')
            else:
                del request.session['otp']
                return redirect('Comp_forgetpass')
        return render(request,'company/login/OTP_CHECK.html')
    else:
        return redirect('c_login') 

def Dashboard(request):
    if 'comp_data' in request.session.keys():
        User = Company_data.objects.get(id = int(request.session['comp_data']))
        
        return render(request,'company/dash/index.html',{'USERS':User})
    else:
        return redirect('c_login')

# ========================== Customer ========================================