from django.shortcuts import render, redirect
from .models import Courses
import datetime


def index(request):
	context = {
	'courses': Courses.objects.all(), # select * from courses

	}
	return render(request, 'courseTemp/index.html', context)

def course(request):
	Courses.objects.create(name=request.POST['name'], description =request.POST['description'] )
	print Courses._meta.db_table
	print(Courses.objects.all())
	return redirect('/')


def destroy(request, id):
	context = {
		'remove': Courses.objects.get(id=id),
	}
	return render(request, 'courseTemp/results.html', context)

def remove(request, id):
	test =  Courses.objects.get(id=id)
	if request.POST[u'button'] == 'Yes! I want to delete this':
		test.delete()
	elif request.POST[u'button'] == 'No':
		pass 
	return redirect('/')

