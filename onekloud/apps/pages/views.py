from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from apps.pages.forms import ContactForm


def home(request):
    ctx = dict()
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
