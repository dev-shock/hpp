from django.shortcuts import render
from .models import Upload

# Create your views here.

def uploadView(request):
	files = Upload.objects.all()
	return render(request, 'portal/index.html', {'files':files})

def downloadView(self):
	files = Download.objects.all()
	return render(request, 'portal/download.html', {'files':files})
