from __future__ import unicode_literals

from django.db import models

class Courses(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	course_id = models.ForeignKey(Courses)

class Post(models.Model):
	title = models.CharField(max_length=45)
	message = models.TextField(max_length=1000)
	# Notice the association made with ForeignKey for a one-to-many relationship
	user_id = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
