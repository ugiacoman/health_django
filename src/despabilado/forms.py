from django import forms

from .models import SignUp

class SignUpForm(forms.ModelForm):

    class Meta:
        model = SignUp
        fields = ["full_name","email"]
        # exclude = ["full_name"]

    def clean_email(self):
        ''' Overload Validation Check for email'''
        email = self.cleaned_data.get("email")
        email_base, provider = email.split("@")
        # domain, extension = provider.split(".")

        if not "edu" in email:
            raise forms.ValidationError("Please use an edu email")
        else:
            return email

    def clean_full_name(self):
        ''' Overload Validation Check for full_name'''
        name = self.cleaned_data.get("full_name")

        if not " " in name:
            raise forms.ValidationError("Please enter both First and Last Name")
        else:
            return name
