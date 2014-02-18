import hashlib
import logging
import urllib.parse

from smtplib import SMTPException
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from apps.pages.forms import SignupForm, ContactForm


def home(request):
    logger = logging.getLogger(__name__)
    ctx = dict()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Email settings.
            subject = "Free trial activation for Onekloud CRM"
            data = form.cleaned_data
            # With this hash we will check if passed data is valid.
            key = '{key}{email}{phone}{company}'.format(
                key=settings.ACTIVATION_SALT, email=data['email'],
                phone=data['phone'], company=data['company']).encode('utf8')
            data['key'] = hashlib.md5(key).hexdigest()

            encdata = urllib.parse.urlencode(data)
            html = mark_safe(render_to_string('pages/activation_email.html',
                                              dict(params=encdata)))
            msg = EmailMessage(
                subject, html, settings.SUPPORT_EMAIL, [data['email']],
                headers={'Reply-To': settings.SUPPORT_EMAIL})
            msg.content_subtype = 'html'
            try:
                msg.send(fail_silently=False)
            except SMTPException as e:
                # Fallback: immediately authorize for Trial with no email
                # notification.
                logger.error(e)
                url = 'https://crm.onekloud.com/auth/activate-trial/'
                full_url = '{url}?{params}'.format(url=url, params=encdata)
                return redirect(full_url)
            else:
                messages.success(
                    request, "Thank you! We have sent you activation link to "
                             "{email}.".format(email=data['email']))
        else:
            messages.error(request, "Your form contains errors.")
    else:
        ctx['form'] = SignupForm()
    return render(request, 'pages/home.html', ctx)


def pricing(request):
    ctx = dict(title="Pricing")
    if request.method == 'POST':
        if 'phone' in request.POST:
            subject = "Someone wants to buy subscription for Onekloud CRM!"
            pricing_type = request.POST['pricing'].capitalize()
            body = "User wants to buy pricing '{type}'.".format(
                type=pricing_type)
            data = dict(email=request.POST['email'],
                        phone=request.POST['phone'],
                        body=body)

            html = mark_safe(render_to_string('pages/email.html', data))
            recipients = ('aldash@onekloud.com', 'samantha@onekloud.com')
            msg = EmailMessage(subject, html, settings.SUPPORT_EMAIL,
                               recipients)
            msg.content_subtype = 'html'
            msg.send()
            messages.success(
                request, "Thank you! We will contact you very soon.")
        else:
            form = SignupForm(request.POST)
            if form.is_valid():
                # Email settings.
                subject = "Free trial activation for Onekloud CRM"
                data = form.cleaned_data

                # With this hash we will check if passed data is valid.
                key = '{key}{email}{company}'.format(
                    key=settings.ACTIVATION_SALT, email=data['email'],
                    company=data['company']).encode('utf8')
                data['key'] = hashlib.md5(key).hexdigest()

                encdata = urllib.parse.urlencode(data)
                html = mark_safe(
                    render_to_string('pages/activation_email.html',
                                     dict(params=encdata)))
                msg = EmailMessage(
                    subject, html, settings.SUPPORT_EMAIL, [data['email']],
                    headers={'Reply-To': settings.SUPPORT_EMAIL})
                msg.content_subtype = 'html'
                msg.send()
                messages.success(
                    request, "Thank you! We have sent you activation link to "
                             "{email}.".format(email=data['email']))
            else:
                messages.error(request, form.errors)
    else:
        ctx['signup_form'] = SignupForm()
    return render(request, 'pages/pricing.html', ctx)


def contact(request):
    ctx = dict(title="Contact")
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            html = mark_safe(render_to_string('pages/email.html', data))
            recipients = ('aldash@onekloud.com', 'samantha@onekloud.com')
            msg = EmailMessage(
                data['subject'], html, data['email'], recipients,
                headers={'Reply-To': data['email']})
            msg.content_subtype = 'html'
            msg.send()
            messages.success(
                request, "Thank you for getting in touch! We will reply you "
                         "within 24 hours.")
        else:
            messages.error(request, form.errors)
    else:
        ctx['form'] = ContactForm()
    return render(request, 'pages/contact.html', ctx)


def privacy(request):
    ctx = dict(title="Privacy Statement")
    return render(request, 'pages/privacy.html', ctx)


def refund(request):
    ctx = dict(title="Refund Policy")
    return render(request, 'pages/refund.html', ctx)


def terms_of_service(request):
    ctx = dict(title="Terms of Service")
    return render(request, 'pages/terms_of_service.html', ctx)


def presentation(request):
    ctx = dict(title="Presentation")
    return render(request, 'pages/presentation.html', ctx)
