from django.urls import path

from .views import index, post_list

urlpatterns = [
    path('', index, name='index'),
    path('post-list/', post_list, name='post-list')
]
