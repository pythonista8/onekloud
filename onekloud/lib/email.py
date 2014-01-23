from smtplib import SMTPException
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


def send_invitation(email_list):
    subject = "Welcome to Onekloud CRM!"
    from_ = 'support@onekloud.com'
    html = mark_safe(render_to_string('onekloud/email/welcome.html'))

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
