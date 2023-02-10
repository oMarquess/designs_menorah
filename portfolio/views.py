from django.shortcuts import render, redirect
from .models import Project
from django.core.mail import mail_admins
from django.contrib import messages



def home(request):
    messages.add_message(request, messages.SUCCESS, 'Your mail has been sent')
    if request.method == 'POST' or None:
        firstname   = request.POST['firstname'],
        lastname    = request.POST['lastname'],
        email       = request.POST['email'],
        #message
        text        = request.POST['text'],        
        subject = 'Customer Enquiry'
        message = 'Name: {}, Lastname: {}, Email: {}, text: {}'.format(firstname, lastname, email, text)
        print(text, firstname, lastname, message)
        mail_admins(subject, message)
        return redirect ('/success')
        
    projects = Project.objects.all()
    
    return render(request, 'portfolio/index.html', {'projects':projects})

def success(request):
    return render(request, 'portfolio/success.html')