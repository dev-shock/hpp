from django.db import models
from datetime import datetime

# Create your models here.
class Upload(models.Model):
	title = models.CharField(max_length=1024)
	time = models.DateField(default=datetime.now)
	file_type = models.CharField(max_length=255)
	file = models.FileField(upload_to='uploads')

	def __str__(self):
		return self.title
	
class Download(models.Model):
	title = models.CharField(max_length=1024)
	time = models.DateField(default=datetime.now)
	file_type = models.CharField(max_length=255)
	url = models.URLField()
	
	def __str__(self):
		return self.title
