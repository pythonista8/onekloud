from django.shortcuts import render


def home(request):
    ctx = dict()
    return render(request, 'pages/home.html', ctx)


def pricing(request):
    ctx = dict(title="Pricing")
    return render(request, 'pages/pricing.html', ctx)


def contact(request):
    ctx = dict(title="Contact")
    return render(request, 'pages/contact.html', ctx)
