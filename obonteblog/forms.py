from django import forms
from . models import Post,Comment,Reply

class AdminForm(forms.ModelForm):
    # password1 = forms.CharField(label=('Password'), widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # password2 = forms.CharField(label=('Confirm Password'), widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['date_posted' ,'published' ,'flag','author']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'leadimg':forms.FileInput(attrs={'class':'form-control','type':'file'}),
        }   


class CommentForm(forms.ModelForm):
    fullname = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Fullname'}))
    body = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Comment here....'}))
    class Meta:
        model = Comment
        fields = ['fullname','body']
        widgets={
            'fullname':forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Fullname'}),
            'body':forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Comment here....'}),
        }  

class ReplyForm(forms.ModelForm):
    body = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Reply comment'}))
    class Meta:
        model = Reply 
        fields = ['body']
        widgets ={
            'body':forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Reply comment'}),
        }