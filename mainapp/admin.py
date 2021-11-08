from django.contrib import admin
from .models import *

admin.site.register(Actor)
admin.site.register(Writer)
admin.site.register(Movie)


prepopulated_fields = {"Actor ": ("actors",)}