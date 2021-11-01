# from django.db.models import fields
from modeltranslation.translator import translator, TranslationOptions
from .models import *


# translation for Headline models
class HeadlineTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', 'story_snippet', 'story')

translator.register(Headline, HeadlineTranslationOptions)

#translation for Profile models
class ProfileTranslationOptions(TranslationOptions):
    fields = ('about_snippet', 'about', 'date')

translator.register(Profile, ProfileTranslationOptions)

# translation for Advert models
class AdvertTranslationOptions(TranslationOptions):
    fields = ('title', 'first_message', 'body', 'slug', 'date')

translator.register(Advert, AdvertTranslationOptions)

# translation for Topstory models
class TopstoryTranslationOptions(TranslationOptions):
    fields = ('title', 'body', 'slug', 'date')

translator.register(Topstory, TopstoryTranslationOptions)