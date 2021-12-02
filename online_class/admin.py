from django.contrib import admin

from .models import Course, Topic, Announcement

admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(Announcement)