from django import forms


class SignupForm(forms.Form):
    email = forms.EmailField()
    phone = forms.CharField()
    company = forms.CharField()

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        res = ''
        for c in phone:
            if c.isdigit() or c.lower() == 'x':
                res += c
        return res


class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)
