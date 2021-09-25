from django.shortcuts import render
from .forms import Form
from .models import Profile, Profile_event_photo, Headline
from django.contrib import messages 
from django.core.paginator import Paginator

# Create your views here.

def home_page(request, *args, **kwargs):
	form = Form(auto_id=False)
	if request.method == 'POST':
		form = Form(request.POST)
		if form.is_valid():
			form.clean()
			form.save()
			messages.success(request, "Your email was received successfully!", fail_silently = True)
	else:
		form = Form()
	context = {
		'form': form
	}
	return render(request, './home/home.html', context)


def events_page(request, *args, **kwargs):
	events_objects = Headline.objects.all().order_by('-date')
	paginate = Paginator(object_list=events_objects, per_page=4, orphans=2, allow_empty_first_page=True)

	page=request.GET.get('page')
	events=paginate.get_page(page)
	form = Form(auto_id=False)
	if request.method == 'POST':
		form = Form(request.POST)
		if form.is_valid():
			form.clean()
			form.save()
			messages.success(request, "Your email was received successfully!", fail_silently = True)
	else:
		form = Form()
	context = {
		'form': form,
		'events': events
	}
	return render(request, './home/events.html', context)


def about_page(request, *args, **kwargs):
	form = Form(auto_id=False)
	if request.method == 'POST':
		form = Form(request.POST)
		if form.is_valid():
			form.clean()
			form.save()
			messages.success(request, "Your email was received successfully!", fail_silently = True)
	else:
		form = Form()
	context = {
		'form': form
	}
	return render(request, './home/about.html', context)


def story_detail(request, slug, *args, **kwargs):
	story = Headline.objects.get(slug = slug)
	form = Form(auto_id=False)
	if request.method == 'POST':
		form = Form(request.POST)
		if form.is_valid():
			form.clean()
			form.save()
			messages.success(request, "Your email was received successfully!", fail_silently = True)
	else:
		form = Form()
	context = {
		'form': form,
		'story': story
	}
	return render(request, './home/story.html', context)


def profile_feed(request, *args, **kwargs):
	profiles = Profile.objects.all().order_by("-date")
	form = Form(auto_id=False)
	if request.method == 'POST':
		form = Form(request.POST)
		if form.is_valid():
			form.clean()
			form.save()
			messages.success(request, "Your email was received successfully!", fail_silently = True)
	else:
		form = Form()
	context = {
		'profiles': profiles,
		'form': form
	}
	return render(request, './home/profile_feed.html', context)


def profile_page(request, slug, *args, **kwargs):
	profiles = Profile.objects.get(slug=slug)
	event_photos = Profile_event_photo.objects.filter(profile=profiles)
	form = Form(auto_id=False)
	if request.method == 'POST':
		form = Form(request.POST)
		if form.is_valid():
			form.clean()
			form.save()
			messages.success(request, "Your email was received successfully!", fail_silently = True)
	else:
		form = Form()
	context = {
		'profiles': profiles,
		'event_photos': event_photos,
		'form': form
	}
	return render(request, './home/profile.html', context)


def donation_page(request, *args, **kwargs):
	form = Form(auto_id=False)
	if request.method == 'POST':
		form = Form(request.POST)
		if form.is_valid():
			form.clean()
			form.save()
			messages.success(request, "Your email was received successfully!", fail_silently = True)
	else:
		form = Form()
	context = {
		'form': form
	}
	return render(request, './home/donate.html', context)