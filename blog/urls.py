from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('posts', views.PostViewSet)
 
 
urlpatterns = [
    path('', include(router.urls)),
    url(r'posts/(?P<pk>\d+)/comments/$', view=views.PostViewSet.as_view({'get':'comments', 'post':'comments'})),
    url(r'posts/(?P<pk>\d+)/comments/(?P<comment>\d+)/$', view=views.PostViewSet.as_view({'delete':'remove_comment'}))
]