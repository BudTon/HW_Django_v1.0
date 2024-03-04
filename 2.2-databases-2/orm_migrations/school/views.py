from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'teachers'
    object_list = Student.objects.prefetch_related(ordering)
    print(object_list)
    context = {'object_list': object_list,}
    return render(request, template, context)
