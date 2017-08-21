# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import UserAvatar
# Create your views here.

def index(request):
	avatar_available_set = UserAvatar.objects.filter(isOccupied = False)
	if(avatar_available_set.count()>0):
		avatar_selected = avatar_available_set[0]
		avatar_selected.isOccupied = True
		avatar_selected.save()
		context = {
			'smartphone_index' : avatar_selected.avatar_index,
			'my_reg_name' : avatar_selected.reg_name,
			'my_d_name' : avatar_selected.d_name
		}
		return render(request, 'Zhuge_smartphone/index.html', context)
	else:
		return render(request, 'Zhuge_smartphone/lobbyfull.html', {})
	
def release_smartphone(request, smartphone_index):
	try:
		avatar_checked = UserAvatar.objects.get(avatar_index = int(smartphone_index))
		avatar_checked.isOccupied = False 
		avatar_checked.save()
		return HttpResponse("release smartphone {}".format(smartphone_index))
	except:
		return HttpResponse("smartphone {} not exist".format(smartphone_index))

def release_all(request):
	try:
		avatar_all = UserAvatar.objects.all()
		for avatar in avatar_all:
			avatar.isOccupied = False
			avatar.save()
		return HttpResponse("all smartphone released.")
	except:
		return HttpResponse("some error happend")

def check_smartphone(request, smartphone_index):
	try:
		avatar_checked = UserAvatar.objects.get(avatar_index = int(smartphone_index))
		if(avatar_checked.isOccupied):
			return HttpResponse("smartphone {} is not available".format(smartphone_index))
		else:
			return HttpResponse("smartphone {} is available".format(smartphone_index))
	except(UserAvatar.DoesNotExist):
		return HttpResponse("smartphone {} not exist".format(smartphone_index))
	

