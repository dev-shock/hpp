from django.shortcuts import render
from .models import Upload
from .forms import UploadForm

# Create your views here.

def uploadView(request):
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
