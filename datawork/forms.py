from django import forms
from .models import *


class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = Admin_login
        fields = '__all__'


class NewUserForm(forms.ModelForm):
    class Meta:
        model = NewUser
        fields = '__all__'


class CategoryForms(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class TopicForms(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'


class PostForms(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ('post_user', 'post_status',)


class PostAdminForms(forms.ModelForm):
    class Meta:
        model = Posts
        fields = "__all__"


class UserProfileEditForms(forms.ModelForm):
    class Meta:
        model = NewUser
        exclude = ('nu_name', 'nu_city', 'nu_state', 'nu_image', 'nu_address', 'nu_email', 'nu_password',)


class UserImageEditForms(forms.ModelForm):
    class Meta:
        model = NewUser
        exclude = ('nu_name', 'nu_city', 'nu_state', 'nu_doc', 'nu_myself', 'nu_address', 'nu_phone', 'nu_email', 'nu_password',)
