from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.views import generic
from django.views.generic import ListView
from .models import Contact


def contact(request):
    if request.method == 'POST':
        name = request.POST['name'] 
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name=name, email=email, phone=phone, subject=subject, message=message)
        contact.save()

        # Send Mail
        send_mail(
            'SUBJECT: '+subject,
            '. Sign into admin panel for more info' "\n\n" 
            "SENDER:  "+ name+ ',' '\n\n' " PHONE NUMBER: "+phone+',' '\n\n' " EMAIL:  "+email+ "\n\n" 
            "MESSAGE: \n\n " + message,
            'ntschangb@gmail.com',
            ['ntschangb@yahoo.com',],
            fail_silently=False
        )

        messages.success(request, ': Your Message has been submitted, an Agent will get back to you soon')
    return render(request, 'pages/contact.html')