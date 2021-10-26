from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    return render(request, 'index.html',{})
    
def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_number = request.POST['message-number']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send email 
        send_mail(
            message_name, # subject
            message, # message
            message_number, # number
            message_email, # from email
            ['danistine1@gmail.com'], # to email
        )

        return render(request, 'contact.html',{'message_name': message_name})

    else:
        return render(request, 'contact.html',{})

def about(request):
    return render(request, 'about.html',{})

def service(request):
    return render(request, 'service.html',{})