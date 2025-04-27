from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path("<int:postId>/", views.post, name='post'),
    path('contact/', views.contact, name='contact'),
]
