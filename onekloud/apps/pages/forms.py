from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)
