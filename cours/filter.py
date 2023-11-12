

from .models import Course
from django_filters import rest_framework as django_filter


class CourseFilter(django_filter.FilterSet):
    class Meta:
        model = Course
        fields = ['degree', 'category']


