EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'thunderboltv10@gmail.com'
EMAIL_HOST_PASSWORD = 'SIRUmiru@10'
EMAIL_PORT = 587

#from django.conf import settings
#from django.core.mail import send_mail

#def send_email_token(email, token):
    #try:
        #subject = 'Your Account needs to be verified'
       #message = f'Click on the link to verify #http://127.0.0.1:8000/verify/{token}/'
        #email_from = settings.EMAIL_HOST_USER
        #recipient_list = [email, ]
        #send_mail( subject, message, email_from, #recipient_list )
    
    #except Exception as e:
        #return False
    
    #return True                