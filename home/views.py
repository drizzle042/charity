from django.shortcuts import render
from django.http import HttpResponse
from .models import Latest_new
from .models import topstorie

# Create your views here.
def home_page(request, *args, **kwargs):
	return render(request, './home/home.html')


def events_page(request, *args, **kwargs):
	story = topstorie.objects.all().order_by('date')
	newsfeed = Latest_new.objects.all().order_by('date')
	return render(request, './home/events.html', {'news':newsfeed, 'detail':story})


def about_page(request, *args, **kwargs):
	return render(request, './home/about.html')


def story_detail(request):
	newsfeed = topstorie.objects.all().order_by('date')	
	return render(request, './home/story.html', {'detail':story_detail, 'news':newsfeed})


def profile_feed(request, *args, **kwargs):
	return render(request, './home/profile_feed.html')


def profile_page(request, *args, **kwargs):
	return render(request, './home/profile.html')


def donation_page(request, *args, **kwargs):
	return render(request, './home/donate.html')