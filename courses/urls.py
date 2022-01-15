from django.contrib import admin
from django.urls import path,include
from courses.view import home,coursepage,signupview,loginview,signout, checkout,verify_payment,mycourses
from django.conf import settings
from django.conf.urls.static import static
from codewithjash.settings import MEDIA_ROOT,MEDIA_URL,STATIC_URL
urlpatterns = [
    path('', home.as_view(), name='home'),
    path('logout/', signout, name='logout'),
    path('signup/', signupview.as_view(), name='signup'),
    path('login/', loginview.as_view(), name='login'),
    path('mycourses/', mycourses.as_view(), name='mycourse'),
    path('courses/<str:slug>', coursepage, name='coursepage'),
    path('check-out/<str:slug>', checkout, name='checkout'),
    path('verify_payment', verify_payment, name='verify_payment'),

]
urlpatterns += static(MEDIA_URL, document_root= MEDIA_ROOT)
urlpatterns += static(STATIC_URL, document_root=settings.STATIC_ROOT)