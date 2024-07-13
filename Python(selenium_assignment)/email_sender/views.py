# submission/views.py

from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.conf import settings

def send_email(request):
    subject = 'Python (Selenium) Assignment - Parth Vichare'  # Replace with your name
    filledform_screenshot_1=r"C:\Users\SIDDESH VICHARE\Downloads\Python Selenium(Assignment)\Python(selenium_assignment)\selenium\filled_form_screenshot1.png"
    filledform_screenshot_2=r"C:\Users\SIDDESH VICHARE\Downloads\Python Selenium(Assignment)\Python(selenium_assignment)\selenium\filled_form_screenshot2.png"
    body = (
        'Hello,\n\n'
        'Please find my submission for the Python (Selenium) assignment attached.\n\n'
        'GitHub Repository: https://github.com/parthvichare/Python-Selenium-Assignment-'
        'Best regards,\n'
        'Parth Vichare'
    )  # Simple message body
    recipient_list = ['parthvichare8@gmail.com']  # Replace with your recipient
    # cc_list = ['parthvichare8@gmail.com']  # CC email

    email = EmailMessage(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        recipient_list,
    )
    email.attach_file(filledform_screenshot_1)
    email.attach_file(filledform_screenshot_2)
    
    # Add CC if needed
    # email.cc = cc_list

    try:
        email.send()
        return HttpResponse("Email sent successfully!")
    except Exception as e:
        return HttpResponse(f"Error sending email: {e}")
