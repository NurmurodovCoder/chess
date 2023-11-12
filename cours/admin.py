from django.contrib import admin
from .models import Lesson, Course, Category, Comment

admin.site.register(Lesson)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Comment)

