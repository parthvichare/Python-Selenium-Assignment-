# Introduction to Project
This project automates form submission using Selenium and implements email functionality in Django. It includes setting up Selenium for browser automation, configuring email settings with Gmail's SMTP server, and sending emails with attachments. The documentation provides step-by-step instructions on setup, usage, challenges faced, and future improvements, ensuring a comprehensive understanding of the project.

# Challenges faced in Selenium Automation
First of all thanks for giving me the opportunity  work on little challenging assignment whcih help me to learn alot about email functionality of django which also enhance my logic thinking 
& problem solving skills

In this automation project I work on selenium first to submit the form and capture screenshots while working on selenium I challenge to get target the element class which is necessary for filling the required details where I use By.Xpath functionality of selenium and use Expected conditions to navigate to the class and fill the detail properly 

Through the filling detail I also create functionality whcih take screenshot where I take 2screenshot of the half pages which in the end I taken the screenshot of successful filling the form 

While working with selenium managing time efficiency and crawling process migh be challenging and quick so where I use webbrowser for to crawling the pages and successfully Filled the form

# Challenges Faced while working on Django Framework with Emailfunctionality
While working on Django Framework I faced challenge to setup the gmail feature through my setting due to changes in email security guidence but I somehow find out how to create App password where we can give access to other third party functionality to send email to the other email user

In views I create an API endpoint, restAPI where I design the email like the body, subject, topic and to whom we have to send the user email_id so I learn to design the email message with the help of django Email functionality

# Here I created the email settings by generating the App password
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Corrected typo
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'parthvichare9@gmail.com'
EMAIL_HOST_PASSWORD = 'oxiz lzfw ghau aoxr'  # Use App Password if 2FA is enabled

