from django.urls import path
from . import views

urlpatterns = [
    
    path('register/', views.register, name='register'),
    path('login/',views.login_view, name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),
 
      # Define join_meeting_view in your views
    path('meeting/', views.video_call, name = 'meeting'),
    path('logout/', views.logout_view, name = 'logout'),
    path('join/', views.join_call, name = 'join'),
]
 