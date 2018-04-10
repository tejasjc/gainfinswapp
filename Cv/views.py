# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def cv_tejas(request):
    return render(request,'Cv/tejasjc.html')

def cv_rushikesh(request):
    return render(request,'Cv/rushikeshsp.html')

def cv_sopan(request):
    return render(request,'Cv/sopanrb.html')

def cv_shubham(request):
    return render(request,'Cv/shubhamlc.html')