from django.urls import path
from . import views 


app_name = 'home'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('events/', views.events_page, name='events'),
    path('story/<slug:slug>/', views.story_detail, name='detail'),
    path('topstory/<slug:slug>/', views.topstories, name='topstory'),
    path('ad/<slug:slug>/', views.advert, name='advert'),
    path('about/', views.about_page, name='about'),
    path('profiles/', views.profile_feed, name='profiles'),
    path('profile/<slug:slug>/', views.profile_page, name='profile'),
    path('donate/', views.donation_page, name='donate'),
    path('receipt/', views.receipt, name='receipt'),
]