from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
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
            recipients = ('aldash@onekloud.com', 'samantha@onekloud.com')
            send_mail(
                data['subject'], data['body'], data['email'], recipients,
                fail_silently=False)
            messages.success(
                request, "Thank you for getting in touch! We will reply you "
                         "within 24 hours.")
        else:
            messages.error(request, form.errors)
    else:
        ctx['form'] = ContactForm()
    return render(request, 'pages/contact.html', ctx)
