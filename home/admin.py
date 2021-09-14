from django.contrib import admin

# Register your models here.
from .models import Latest_new
from .models import topstorie


admin.site.register(Latest_new)
admin.site.register(topstorie)
