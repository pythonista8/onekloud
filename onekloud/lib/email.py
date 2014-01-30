from smtplib import SMTPException
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


def send_invitation(email_list):
    MAX_NUMBER = 50

    subject = "Welcome to Onekloud CRM!"
    from_ = 'support@onekloud.com'
    html = mark_safe(render_to_string('onekloud/email/welcome.html'))

    if len(email_list) > MAX_NUMBER:
        raise ValueError(
            "Number of emails must not exceed {}.".format(MAX_NUMBER))

    for i, email in enumerate(email_list):
        msg = EmailMessage(subject, html, from_, [email],
                           headers={'Reply-To': from_})
        msg.content_subtype = 'html'
        print("{i} out of {total}: {email}".format(
            i=i + 1, total=len(email_list), email=email))
        try:
            msg.send(fail_silently=False)
        except SMTPException as err:
            print(err)
        else:
            print("Sent")
