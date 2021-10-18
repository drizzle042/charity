from django.urls import path
from . import views 
from django.utils.translation import gettext_lazy as _


app_name = 'home'

urlpatterns = [
    path('', views.home_page, name='home'),
    path(_('events/'), views.events_page, name='events'),
    path(_('story/<slug:slug>/'), views.story_detail, name='detail'),
    path(_('topstory/<slug:slug>/'), views.topstories, name='topstory'),
    path(_('ad/<slug:slug>/'), views.advert, name='advert'),
    path(_('about/'), views.about_page, name='about'),
    path(_('profiles/'), views.profile_feed, name='profiles'),
    path(_('profile/<slug:slug>/'), views.profile_page, name='profile'),
    path(_('donate/'), views.donation_page, name='donate'),
    path(_('receipt/'), views.receipt, name='receipt'),
]