from django.conf.urls import url
from .views import uploadView 
urlpatterns = [
	url(r'^$', uploadView ,name='upload_view')

]