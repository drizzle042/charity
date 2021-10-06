from django.contrib import admin
from .models import Email, Followers_email, Profile, Profile_event_photo, Headline, Advert, Advert_image, Topstory, Topstory_image 

class Inline_stack(admin.StackedInline):
    model = Profile_event_photo

class Advert_images_stacked(admin.StackedInline):
    model = Advert_image

class Topsstory_images_stacked(admin.StackedInline):
    model = Topstory_image

# Register your models here.
admin.site.register(Email),

admin.site.register(Headline),

admin.site.register(Followers_email),

@admin.register(Profile)
class Inline(admin.ModelAdmin):
    inlines = [Inline_stack]

    class Meta:
        model = Profile

@admin.register(Profile_event_photo)
class Inline_stack(admin.ModelAdmin):
    pass

@admin.register(Advert)
class Inline(admin.ModelAdmin):
    inlines = [Advert_images_stacked]

    class Meta:
        model = Advert

@admin.register(Advert_image)
class Advert_images_stacked(admin.ModelAdmin):
    pass

@admin.register(Topstory)
class Inline(admin.ModelAdmin):
    inlines = [Topsstory_images_stacked]

    class Meta:
        model = Topstory

@admin.register(Topstory_image)
class Topstory_image_stacked(admin.ModelAdmin):
    pass