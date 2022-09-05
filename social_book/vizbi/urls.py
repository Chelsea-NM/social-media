from django.urls import include, path
from . import views
from rest_framework import routers

from .views import ProfileViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r'profile', ProfileViewSet)
router.register(r'post', PostViewSet)

urlpatterns = [
   path('api/', include(router.urls)),
   path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
]