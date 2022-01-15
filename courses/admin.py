from django.contrib import admin
from django.db import models
from courses.models import Course,Tag,Prerequisite,Learning,Usercourse, Payment
from courses.models import Video
from django.utils.html import format_html
# Register your models here.

#make an inline form

class TagAdmin(admin.TabularInline):
    model = Tag


class LearningAdmin(admin.TabularInline):
    model = Learning


class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite

class VideoAdmin(admin.ModelAdmin):
    model = Video
    list_display =['title','course','serial_number','is_preview']
    list_filter = ['course','is_preview']

class courseAdmin(admin.ModelAdmin):
    inlines =[TagAdmin,LearningAdmin,PrerequisiteAdmin]
    
    list_display = ['name', 'get_price','get_discount','active']
    list_filter =['discount','active']
    def get_discount(self,course):
        return f'{course.discount}%'

    def get_price(self,course):
        return f'₹ {course.price}'

    get_discount.short_description = 'Discount'
    get_price.short_description = 'Price'

class PaymentAdmin(admin.ModelAdmin):
    model = Payment

    list_display = ['order_id','get_user','get_course','status']
    list_filter =['status','course']

    def get_user(self, payment):
        return format_html(f"<a target='_blank' href='admin/auth/user/{payment.user.id}/'>{payment.user}</a>")

    def get_course(self, payment):
        return format_html(f"<a target='_blank' href='admin/courses/course/{payment.course.id}/'>{payment.course}</a>")

    get_user.short_description = 'User'
    get_course.short_description ='Course'

class UsercourseAdmin(admin.ModelAdmin):
    model = Usercourse

    list_display = ['user', 'course']
    list_filter =['course']


admin.site.register(Course,courseAdmin)
admin.site.register(Video,VideoAdmin)
admin.site.register(Payment,PaymentAdmin)
admin.site.register(Usercourse,UsercourseAdmin)

