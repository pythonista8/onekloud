from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


def send_invitation(email_list):
    subject = "Welcome to Onekloud CRM!"
    from_ = 'support@onekloud.com'
    html = mark_safe(render_to_string('onekloud/email/welcome.html'))

    for email in email_list:
        msg = EmailMessage(subject, html, from_, [email],
                           headers={'Reply-To': from_})
        msg.content_subtype = 'html'
        msg.send(fail_silently=True)
