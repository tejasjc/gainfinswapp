# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# from django.core.mail import EmailMessage
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request,'Home/index.html')

def sendm(request):
    # email = EmailMessage('Subject', 'Body', to=['tejasjc@gmail.com'])
    # email.send()
    name=request.POST['name']
    mail=request.POST['email']
    msg=request.POST['message']
    msgn=msg+"\n"+mail
    send_mail(name, msgn, 'tejasjc@gmail.com', ['tejasjc@gmail.com'], fail_silently=False)

    return render(request, 'Home/index.html')