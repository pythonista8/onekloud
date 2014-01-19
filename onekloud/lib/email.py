from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


def send_invitation(email_list):
    html = mark_safe(render_to_string('onekloud/email/welcome.html', dict()))
    subject = 'Blah'
    support_email = 'support@onekloud.com'
    for email in email_list:
        msg = EmailMessage(
            subject, html, support_email, ['aldash@onekloud.com'],
            headers={'Reply-To': support_email})
        msg.content_subtype = 'html'
        msg.send()
