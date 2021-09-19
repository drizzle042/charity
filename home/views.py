from django.shortcuts import render
from .forms import Form
from .models import Profile, Profile_event_photo

# Create your views here.

def home_page(request, *args, **kwargs):
	form = Form(auto_id=False)
	if request.method == 'POST':
		form = Form(request.POST)
		if form.is_valid():
			form.clean()
			form.save()
	else:
		form = Form()
	return render(request, './home/home.html', {'form': form})


def events_page(request, *args, **kwargs):
	form = Form(auto_id=False)
	if request.method == 'POST':
		form = Form(request.POST)
		if form.is_valid():
			form.clean()
			form.save()
	else:
		form = Form()
	return render(request, './home/events.html', {'form': form})


def about_page(request, *args, **kwargs):
	form = Form(auto_id=False)
	if request.method == 'POST':
		form = Form(request.POST)
		if form.is_valid():
			form.clean()
			form.save()
	else:
		form = Form()
	return render(request, './home/about.html', {'form': form})


def story_detail(request, *args, **kwargs):
	form = Form(auto_id=False)
	if request.method == 'POST':
		form = Form(request.POST)
		if form.is_valid():
			form.clean()
			form.save()
	else:
		form = Form()
	return render(request, './home/story.html', {'form': form})


def profile_feed(request, *args, **kwargs):
	profiles = Profile.objects.all()
	form = Form(auto_id=False)
	if request.method == 'POST':
		form = Form(request.POST)
		if form.is_valid():
			form.clean()
			form.save()
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
	else:
		form = Form()
	return render(request, './home/donate.html', {'form': form})