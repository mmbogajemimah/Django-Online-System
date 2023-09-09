from django.urls import path
from . import views

# Maps urls to certain locations
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
