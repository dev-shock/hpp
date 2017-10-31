from django.conf.urls import url
from .views import uploadView, downloadView
urlpatterns = [
	url(r'^$', uploadView ,name='upload_view'),
	url(r'^download_list/$', downloadView, name='download_view')

]
