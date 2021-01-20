from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime, date

# Create your models here.

class Category(models.Model):
	name=	models.CharField(max_length= 30)

	def __str__(self):
		return self.name	

	def get_absolute_url(self):
		return reverse("home")


class Article(models.Model):
	title=	models.CharField(max_length= 30, null=False)
	author=  models.ForeignKey(User, on_delete= models.CASCADE)
	content=	models.TextField()
	post_date= models.DateField(auto_now_add= True)
	category=	models.CharField(max_length= 30, default= 'Uncategorised')
	likes= models.ManyToManyField(User, related_name='blog_posts')

	def __str__(self):
		return self.title + ' | ' + str(self.author)	

	def get_absolute_url(self):
		return reverse("article-detail", kwargs={"my_id": self.id})

	