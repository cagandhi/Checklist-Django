from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from djrichtextfield.models import RichTextField


class Checklist(models.Model):
	title = models.CharField(max_length=100)
	# content = models.TextField()

	# https://pypi.org/project/django-richtextfield/ - to store rich text in database [ GitHub: https://github.com/jaap3/django-richtextfield ]
	content = RichTextField() 
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	visibility = models.IntegerField(default=0)
	category = models.ForeignKey('Category', null=True, on_delete = models.SET_NULL)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('checklist-detail', kwargs={'pk': self.id})


class Upvote(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username + " - " + self.checklist.title


class Bookmark(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username + " - " + self.checklist.title


class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name
