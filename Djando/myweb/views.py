# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from .models import myweb_tabl

# Create your views here.



def index(request):
	return render (request, 'myweb/home.html')


def add(request):
	return render (request, 'myweb/add.html')


def show(request):
	all_data = myweb_tabl.objects.all()
	return render (request, 'myweb/show.html',{'data':['name','addddd'] })

