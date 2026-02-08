from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('cbv/', views.WelcomeView.as_view(), name='cbv'),
    path('posts/', views.post_titles, name='posts'),


]
