import sys
import urllib

from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from lib.encrypt import hmac_sha256
from apps.pages.forms import SignupForm, ContactForm


def home(request):
    ctx = dict()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            hash_ = hmac_sha256(
                '{email}{key}{company}'.format(key=settings.HMAC_KEY,
                                               email=data['email'],
                                               company=data['company']))
            url = 'https://crm.onekloud.com/auth/create_user'
            req = urllib.request.Request(url, data=data,
                                         origin_req_host=settings.HOST_IP)
            req.add_header('Authorization', hash_)
            req.add_header('Content-Length', sys.getsizeof(data))
            resp = urllib.request.urlopen(req).read()
            if resp.status_code == 200:
                messages.success(request, "Success!")
            else:
                messages.error(request, "Error!")
    else:
        ctx['form'] = SignupForm()
    return render(request, 'pages/home.html', ctx)


def pricing(request):
    ctx = dict(title="Pricing")
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
