from django import forms
from django.contrib.auth import get_user_model
from django.core import validators

User = get_user_model()


class ContactForm(forms.Form):

    fullname= forms.CharField(
        widget=forms.TextInput(attrs={'type':"text", 'aria-required':"true", 'name':"widget-contact-form-name", 'class':"form-control required name",'placeholder':"Enter your Full Name"})
        ,label="",
        validators=[
            validators.MaxLengthValidator(20,'Full name is Too long!'),
            validators.MinLengthValidator(4,'Full name is Too short!')])
            

    email = forms.EmailField(
        widget= forms.TextInput(attrs={"type":"text", "aria-required":"true", "name":"widget-contact-form-email", "class":"form-control required name","placeholder":"Enter your Email"}),
        label="")
    
    phone= forms.CharField(
        widget=forms.TextInput(attrs={"type":"text", "aria-required":"true", "name":"widget-contact-form-phone", "class":"form-control required name","placeholder":"Enter your Phone Number"})
        ,label="",
        validators=[
            validators.MaxLengthValidator(15,'Phone Number is not valid')])


    subject= forms.CharField(
        widget=forms.TextInput(attrs={"type":"text", "aria-required":"true", "name":"widget-contact-form-subject", "class":"form-control required name","placeholder":"Enter the Subject"})
        ,label="",
        validators=[
            validators.MaxLengthValidator(50,'Subject is Too long!'),
            validators.MinLengthValidator(4,'Subject is Too short!')])

    text= forms.CharField(
        widget=forms.Textarea(attrs={"type":"text", "aria-required":"true", "name":"widget-contact-form-message", "class":"form-control required", "placeholder":"Enter your message...","rows":"8",'style':"resize: none;"})
        ,label="")

    # def clean_email(self):
    #             if 'subscribe' in self.data:
    #                     email = self.cleaned_data.get('email')
    #                     qs = Subscription.objects.filter(email=email)
    #                     if qs.exists():
    #                             raise forms.ValidationError("You are already subscribed.")
    #                     return email