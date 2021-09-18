from django.forms import ModelForm
from .models import Email

class Form(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'email', 'placeholder': 'Enter Your Email Here...'})
        self.fields['email'].label=''
    class Meta:
        model = Email
        fields = '__all__'