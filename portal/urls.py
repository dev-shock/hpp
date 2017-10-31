from django.conf.urls import url
from .views import uploadView, uploadFormView, downloadView
urlpatterns = [
	url(r'^$', uploadView ,name='upload_view'),
 	url(r'^download_list/$', downloadView, name='download_view'),
	url(r'^upload/$', uploadFormView ,name='upload_form_view'),
]
