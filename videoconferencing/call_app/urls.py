from django.urls import path
from . import views

urlpatterns = [
    
    path('register/', views.register, name='register'),
    path('login/',views.login_view, name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('new-meeting/', views.new_meeting_view, name='new_meeting'),  # Define new_meeting_view in your views
    path('join-meeting/', views.join_meeting_view, name='join_meeting'),  # Define join_meeting_view in your views
    # path('logout/', views.logout_view(), name='logout'),
]
 