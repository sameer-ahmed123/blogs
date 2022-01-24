from django import forms
from .models import Comment,blog

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

        widgets ={
            'name': forms.TextInput(attrs={'class':'form-control','required':True}),
            'email':forms.EmailInput(attrs={'class':'form-control','required':True}),
            'body':forms.Textarea(attrs={'class':'form-control','required':True})
        }


class Blogform(forms.ModelForm):
    class Meta:
        model=blog
        fields =['title','slug','intro','body','writer']

        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control','required':True}),
            'slug':forms.TextInput(attrs={'class':'form-control','required':True}),
            'intro':forms.Textarea(attrs={'class':'form-control','required':True}),
            'body':forms.Textarea(attrs={'class':'form-control','required':True}),
            'writer':forms.TextInput(attrs={'class':'form-control','required':True})

        }
