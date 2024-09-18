import logging
from django.core.mail import send_mail
from django.conf import settings

logger = logging.getLogger('email')
def send_notification_email(subject, message, recipient_list):        
    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            recipient_list,
            fail_silently=False,
        )
        logger.info(f"Email sent successfully to {recipient_list}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")