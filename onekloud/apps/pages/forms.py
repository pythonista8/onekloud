from django import forms


class SignupForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    company = forms.CharField()


class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)
