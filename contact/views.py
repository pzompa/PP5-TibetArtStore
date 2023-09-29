from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages
from datetime import datetime


def contact_us(request):
    form = ContactForm()  # Create a new instance of the form
    return render(request, 'contact/contact_us.html', {'form': form})


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST, user=request.user)
        if form.is_valid():
            instance = form.save()
            # Send email
            subject = "Thank you for contacting us."
            message = """
            <p>Your name: {name}</p>
            <p>Your email: {email}</p>
            <p style="text-decoration: underline; font-style: italic;">Your comment details:</p>
            <p>Your comment: {comment}</p>
            <p>Date and Time: {date_time}</p>
            <p>(We usually respond within 24 hours. If you need urgent assistance, please call us at 0049-17344050594)</p>
            """.format(
                name=instance.name,
                email=instance.email,
                comment=instance.comment,
                date_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            )

            send_mail(
                subject,
                "",
                settings.DEFAULT_FROM_EMAIL,
                [instance.email],
                fail_silently=False,
                html_message=message
            )
            # Or wherever you want to redirect after successful submission
            return render(request, 'contact/thank_you_contact.html', {'name': instance.name, 'comment': instance.comment})
    else:
        form = ContactForm()

    return render(request, 'contact/contact_form.html', {'form': form})

