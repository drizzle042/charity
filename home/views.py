from django.shortcuts import render
from .forms import Form

# Create your views here.
def home_page(request, *args, **kwargs):
	form = Form
	if request.method == 'POST':
		form = Form(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = Form()
	return render(request, './home/home.html', {'form': form})


def events_page(request, *args, **kwargs):
	form = Form
	if request.method == 'POST':
		form = Form(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = Form()
	return render(request, './home/events.html', {'form': form})


def about_page(request, *args, **kwargs):
	form = Form
	if request.method == 'POST':
		form = Form(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = Form()
	return render(request, './home/about.html', {'form': form})


def story_detail(request, *args, **kwargs):
	form = Form
	if request.method == 'POST':
		form = Form(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = Form()
	return render(request, './home/story.html', {'form': form})


def profile_feed(request, *args, **kwargs):
	form = Form
	if request.method == 'POST':
		form = Form(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = Form()
	return render(request, './home/profile_feed.html', {'form': form})


def profile_page(request, *args, **kwargs):
	form = Form
	if request.method == 'POST':
		form = Form(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = Form()
	return render(request, './home/profile.html', {'form': form})


def donation_page(request, *args, **kwargs):
	form = Form
	if request.method == 'POST':
		form = Form(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = Form()
	return render(request, './home/donate.html', {'form': form})