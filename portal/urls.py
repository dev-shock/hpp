from django.conf.urls import url
from .views import index, uploadFormView 

app_name = 'portal'

urlpatterns = [
	url(r'^$', index ,name='index'),
	url(r'^upload/$', uploadFormView ,name='upload_form_view')

]