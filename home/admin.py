from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *

# Translation class
class Translation(TranslationAdmin):
    pass

# classes for StackedInline
class Profile_images_stacked(admin.StackedInline):
    model = Profile_event_photo

class Advert_images_stacked(admin.StackedInline):
    model = Advert_image

class Topsstory_images_stacked(admin.StackedInline):
    model = Topstory_image

# Register your models here.
admin.site.register(Email),


admin.site.register(Headline, Translation),

admin.site.register(Followers_email),

admin.site.register(Profile, Translation)
class Inline(admin.ModelAdmin):
    inlines = [Profile_images_stacked]
    
    class Meta:
        model = Profile

@admin.register(Profile_event_photo)
class Profile_images_stacked(admin.ModelAdmin):
    pass

admin.site.register(Advert, Translation)
class Inline(admin.ModelAdmin):
    inlines = [Advert_images_stacked]

    class Meta:
        model = Advert

@admin.register(Advert_image)
class Advert_images_stacked(admin.ModelAdmin):
    pass

admin.site.register(Topstory, Translation)
class Inline(admin.ModelAdmin):
    inlines = [Topsstory_images_stacked]

    class Meta:
        model = Topstory

@admin.register(Topstory_image)
class Topstory_image_stacked(admin.ModelAdmin):
    pass