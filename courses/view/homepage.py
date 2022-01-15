from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Course
from django.views.generic import ListView


class home(ListView):
    template_name = 'courses/home.html'
    context_object_name ='courses'

    def get_queryset(self):
        return Course.objects.filter(active = True) 

'''
def home(request):
    courses = Course.objects.all()
    
    return render(request,'courses/home.html', context={'courses':courses}) 

'''