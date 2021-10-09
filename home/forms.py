from django.forms import ModelForm
from .models import Email, Followers_email

class Form(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label=''
        self.fields['email'].widget.attrs.update({
            'class': 'email', 
            'placeholder': 'Enter Your Email Here...'
            })
    class Meta:
        model = Email
        fields = '__all__'


class Followers_email_form(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label=''
        self.fields['email'].widget.attrs.update({
            'class': 'email', 
            'placeholder': 'Enter Your Email Here...'
            })
        self.fields['profile'].label=''
        self.fields['profile'].widget.attrs.update({
            'class': 'profile'
        })
    class Meta:
        model = Followers_email
        fields = '__all__'