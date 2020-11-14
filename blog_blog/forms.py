from tinymce.widgets import TinyMCE
from django import forms
from .models import Comment, Post
from django.core import validators
from tinymce import HTMLField
from ckeditor.widgets import CKEditorWidget

class CommentForm(forms.Form):
    name= forms.CharField(
        widget=forms.TextInput(attrs={'type':"text", 'aria-required':"true", 'name':"widget-contact-form-name", 'class':"form-control required name",'placeholder':"Enter your Name"})
        ,label="",
        validators=[
            validators.MaxLengthValidator(20,'Name is Too long!')])
            
    email = forms.EmailField(
        widget= forms.TextInput(attrs={"type":"text", "aria-required":"true", "name":"widget-contact-form-email", "class":"form-control required name","placeholder":"Enter your Email"}),
        label="")


    body= forms.CharField(
        widget=forms.Textarea(attrs={"type":"text", "aria-required":"true", "name":"widget-contact-form-message", "class":"form-control required", "placeholder":"Enter your comment...","rows":"8",'style':"resize: none;"})
        ,label="")


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('body',)

    # class Media:
    #     js = ('/Users/hosseinshakiba/Desktop/MyBlog/static_cdn/static_root/tinymce/js/tinymce/tinymce.min.js')
    #     css = ('')
    # body = forms.CharField(widget=TinyMCE(mce_attrs={'width': 800}))
    # body = HTMLField('body')
    # body = forms.CharField(widget=CKEditorWidget())
