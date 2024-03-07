from django.urls import path
from . import views
urlpatterns = [
    path('/', views.main, name='main'),
    path('/about',views.about, name='about'),
    path('/profile',views.profile, name='profile'),
    path('/chat',views.chat, name='chat'),
]
