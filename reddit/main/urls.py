from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^data/', views.data, name = 'data'),
        url(r'^posts/([0-9]+)/$', views.posts, name = 'posts'),
        url(r'^index/', views.index, name = 'index'),
]
