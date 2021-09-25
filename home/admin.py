from django.contrib import admin
from .models import Email, Profile, Profile_event_photo, Headline 

class Inline_stack(admin.StackedInline):
    model = Profile_event_photo
# Register your models here.
admin.site.register(Email),

admin.site.register(Headline),

@admin.register(Profile)
class Inline(admin.ModelAdmin):
    inlines = [Inline_stack]

    class Meta:
        model = Profile

@admin.register(Profile_event_photo)
class Inline_stack(admin.ModelAdmin):
    pass