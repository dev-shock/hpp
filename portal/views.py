from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Upload, Download
from .forms import UploadForm

# Create your views here.

def index(request):
	files = Upload.objects.all()
	return render(request, 'portal/index.html', {'files':files})

def uploadFormView(request):
	if request.method == 'POST':
		upload_form = UploadForm(data=request.POST)

		if upload_form.is_valid():
			uploadForm = upload_form.save()

			return HttpResponseRedirect(reverse('uploadView'))

	else:
		upload_form = UploadForm()
	return render(request, 'portal/upload.html', {'upload_form': upload_form})

def downloadView(self):
	files = Download.objects.all()
	return render(request, 'portal/download.html', {'files':files})
