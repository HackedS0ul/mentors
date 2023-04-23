from django.contrib import admin
from .models import User, Course, Rating


admin.site.register(User)
admin.site.register(Course)
admin.site.register(Rating)