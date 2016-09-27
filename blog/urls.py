#importem llibreries
from django.conf.urls import include, url 

#importem vistes
from .import views 

urlpatterns = [
	url (r'^$',views.post_list),
]

