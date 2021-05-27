from django.urls import path

from .views import index, post_list, post_detail

urlpatterns = [
    path('', index, name='index'),
    path('post-list/', post_list, name='post-list'),
    path('post-detail/<int:id>/', post_detail, name='post_detail')
]
