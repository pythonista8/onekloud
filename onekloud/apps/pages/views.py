import hashlib
import urllib.parse

from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from apps.pages.forms import SignupForm, ContactForm

SUPPORT_EMAIL = 'support@onekloud.com'


def home(request):
    ctx = dict()
    if request.method == 'POST':
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
            html = mark_safe(render_to_string('pages/activation_email.html',
                                              dict(params=encdata)))
            msg = EmailMessage(
                subject, html, SUPPORT_EMAIL, [data['email']],
                headers={'Reply-To': SUPPORT_EMAIL})
            msg.content_subtype = 'html'
            msg.send()
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
            msg = EmailMessage(subject, html, SUPPORT_EMAIL, recipients)
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
                    subject, html, SUPPORT_EMAIL, [data['email']],
                    headers={'Reply-To': SUPPORT_EMAIL})
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


def terms_of_service(request):
    ctx = dict(title="Terms of Service")
    return render(request, 'pages/terms_of_service.html', ctx)
