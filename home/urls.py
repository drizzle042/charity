from django.urls import path
from . import views 


app_name = 'home'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('events/', views.events_page, name='events'),
    path('story/', views.story_detail, name='detail'),
    path('about/', views.about_page, name='about'),
    path('profiles/', views.profile_feed, name='profiles'),
    path('donate/', views.donation_page, name='donate'),
    path('profile/<slug:slug>/', views.profile_page, name='profile'),
]