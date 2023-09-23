from django.shortcuts import render
from django.core.mail import EmailMessage, get_connection
from django.core.mail import BadHeaderError
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail

def contact_us(request):
    return render(request, 'contact/contact_us.html')


def send_email2(request):
    try:
        if request.method == "POST":
            with get_connection(
            host=settings.EMAIL_HOST, 
        port=settings.EMAIL_PORT,  
        username=settings.EMAIL_HOST_USER, 
        password=settings.EMAIL_HOST_PASSWORD, 
        use_tls=settings.EMAIL_USE_TLS  
            ) as connection:  
                subject = request.POST.get("subject")  
                email_from = settings.EMAIL_HOST_USER  
                recipient_list = request.POST.get("email")
                message = request.POST.get("message")  
                print(EmailMessage(subject, message, email_from, recipient_list, connection=connection).send())
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    except Exception as e:
        # This will print the error message to the console
        print(f"Error: {e}")
        # This will return the error as an HTTP response
        # Useful for debugging, but not recommended for production
    return render(request, 'products/products_list.html')


def send_email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['lodentashi@hotmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('redirect to a new page')