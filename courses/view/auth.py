from django import views
from django.shortcuts import redirect, render
from courses import view
from courses.models import Course,Video
from django.http import HttpResponse
from courses.forms import Registrationform, Loginform
from django.views import View
from django.contrib.auth import logout, login
from django.views.generic.edit import  FormView



# form view signup code
class signupview(FormView):
    template_name = "courses/signup.html"
    form_class = Registrationform
    success_url ='/login/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)



class loginview(FormView):
    template_name = "courses/login.html"
    form_class = Loginform
    success_url ='/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        login(self.request,form.cleaned_data)
        next_page = self.request.GET.get('next')
        if next_page is not None:
            return redirect(next_page)
        return super().form_valid(form)





## Class based signup view

'''
class signupview(View):
    def get(self,request):
        form = Registrationform()
        return render(request, template_name= "courses/signup.html", context={'form' : form })

    def post(self, request):
        form = Registrationform(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('login')

        return render(request, template_name= "courses/signup.html", context={'form' : form })

'''

## Basic signupcode
'''
def signup(request):
    if request.method == 'GET':    
        form = Registrationform()
        return render(request, template_name= "courses/signup.html", context={'form' : form })
    

    form = Registrationform(request.POST)
    if form.is_valid():
        user = form.save()
        if user is not None:
            return redirect('login')

    return render(request, template_name= "courses/signup.html", context={'form' : form })

## basic login code

def login(request):
    return render(request,"courses/login.html")

'''


'''
# class bases login code
class loginview(View):
    def get(self, request):
        form = Loginform()
        context = {
            'form': form
        }
        return render(request,"courses/login.html", context = context)

    def post(self, request):
        form = Loginform(request = request, data = request.POST)
        context = {
            'form': form
        }
        
        if form.is_valid():
            return redirect('home')
        
        return render(request,"courses/login.html", context = context)
'''

## Logout Coding

def signout(request):
    logout(request)
    return redirect('home')


