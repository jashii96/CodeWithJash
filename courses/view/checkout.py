from django import http
from django.shortcuts import render,redirect
from courses.models import Course,Video, Payment, Usercourse, payment
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from codewithjash.settings import *
from time import time
from django.contrib.auth.decorators import login_required
import razorpay


client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))

@login_required(login_url='login')
def checkout(request,slug):
    course = Course.objects.get(slug = slug)
    #user = None
    #if request.user.is_authenticated is False:
     #   return redirect("login")

## Data Creation To Pass while creating order
    user = request.user
    action = request.GET.get('action')
    order = None
    payment = None
    error = None
    if action == 'create_payment':
        try:
            user_course = Usercourse.objects.get(user = user, course = course)
            error = "You Are Already Enrolled These Course!!!"
        except:
            pass

        if error is None:
            
            amount = int((course.price - (course.price * course.discount * 0.01)) * 100)
            currency = "INR"
            notes = {
                "email" : user.email,
                "name" : f'{user.first_name} {user.last_name}'
            }
            receipt = f"codewithjash-{int(time())}"

    ## Razorpay Dictionary Pass for Order Creations
            order=client.order.create({
            'receipt' : receipt,
            'notes' : notes, 
            'amount' : amount, 
            'currency' : currency
            }
            )
    ## Create payment object and save data in database
            payment = Payment()
            payment.user = user
            payment.course = course
            payment.order_id = order.get('id')
            payment.save()

    context = {
        "course" : course,
        "order" : order,
        "payment" : payment,
        "user" : user,
        "error" : error
     }
    return render(request,'courses/check-out.html', context = context)


@csrf_exempt
def verify_payment(request):
    if request.method == 'POST':
        data = request.POST
        context={}
        try:
            client.utility.verify_payment_signature(data)
            razorpay_order_id = data['razorpay_order_id']
            razorpay_payment_id = data['razorpay_payment_id']
            payment = Payment.objects.get(order_id = razorpay_order_id)
            payment.payment_id = razorpay_payment_id
            payment.status = True

            usercourse = Usercourse(user = payment.user , course = payment.course)
            usercourse.save()

            payment.user_course = usercourse
            payment.save()

            return redirect('mycourse')
        except:
            return HttpResponse("Invalid Payment Details")