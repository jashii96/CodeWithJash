from django.shortcuts import render,redirect
from courses.models import Course,Video,Usercourse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.utils.decorators import method_decorator

@method_decorator(login_required(login_url='login'), name= 'dispatch')
class mycourses(ListView):
    template_name = 'courses/my_course.html'
    context_object_name = 'user_course'

    def get_queryset(self):
        return Usercourse.objects.filter(user = self.request.user)



'''
# basic method
@login_required(login_url='login')
def mycourses(request):
    user =request.user
    user_course = Usercourse.objects.filter(user = user)
    context = {
        'user_course': user_course
    }
    return render(request,'courses/my_course.html', context= context)

'''




def coursepage(request,slug):
    course = Course.objects.get(slug = slug)
    serial_number = request.GET.get('lecture')
    videos = course.video_set.all().order_by("serial_number")
    if serial_number is None:
        serial_number = 1
    video = Video.objects.get(serial_number = serial_number, course = course)
    


    if (video.is_preview is False):

        if request.user.is_authenticated is False:
            return redirect("login")

        else:
            user = request.user
            try:
                user_course = Usercourse.objects.get(user = user, course = course)
                
            except:
                return redirect("checkout", slug = course.slug)
                
    
    
    
    
    
    context = {
        "course" : course,
        "video" : video,
        "videos" : videos
    }
    return render(request,'courses/course_page.html', context=context)


