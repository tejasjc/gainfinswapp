# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from django.core.mail import EmailMessage
from django.core.mail import send_mail
import json


# Create your views here.
def index(request):
    return render(request,'Home/index.html')

@csrf_exempt
def sendm(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        message = request.POST.get('message')
        response_data = {}
        email_body="Name:"+name+"\nMobile Number:"+str(mobile)+"\nEmail:"+email+"\nMessage:\n"+message
        try:
            send_mail("Contact Request",email_body,"gainfinswebapp@gmail.com",["tejasjc@gmail.com","rushikeshsp25@gmail.com","7177sc@gmail.com","sopanbembde@gmail.com"])
        except:
            response_data['result'] = 'Error occured at server site , try again in sometime , Or Try calling (+91-7775910607) Or Drop an email @ (contact@gainfins.com)'
        else:
            response_data['result'] = 'Thank you ' + name + ', Our team will contact you soon !'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

