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
    confirmation_screenshot=r"C:\Users\SIDDESH VICHARE\Downloads\Python Selenium(Assignment)\Python(selenium_assignment)\selenium\Screenshot after submission.png"
    
    # Documentation of the Projecct Assignment
    documentation=r"C:\Users\SIDDESH VICHARE\Downloads\Python Selenium(Assignment)\Python(selenium_assignment)\readme.md" 
    
    body = (
    'Hello Medius-Team,\n\n'
    'Thanks for giving me the opportunity to perform the assignment.\n\n'
    'Please take look of attached files:\n'
    '- Screenshot of the filled form 1: filled_form_screenshot1.png\n'
    '- Screenshot of the filled form 2: filled_form_screenshot2.png\n'
    '- Confirmation of submission: Screenshot after submission.png\n'
    '- Project documentation: readme.md\n\n'
    'GitHub Repository (source code): https://github.com/parthvichare/Python-Selenium-Assignment-\n\n'
    'Best regards,\n'
    'Parth Vichare'
     )
    recipient_list = ['tech@themedius.ai']  
    cc_list = ['hr@themedius.ai']  # CC email

    email = EmailMessage(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        recipient_list,
    )
    email.attach_file(filledform_screenshot_1)
    email.attach_file(filledform_screenshot_2)

    #Confirmation of Submission form succesfully
    email.attach_file(confirmation_screenshot)

    email.attach_file(documentation)
    
    # Add CC if needed
    email.cc = cc_list

    try:
        email.send()
        return HttpResponse("Email sent successfully!")
    except Exception as e:
        return HttpResponse(f"Error sending email: {e}")
