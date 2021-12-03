from django.contrib.auth.models import User
from django import forms
# from .models import Profile
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from .models import UserRegistrationModel
from django.contrib.auth.forms import PasswordResetForm
from django.forms import ModelForm
from online_class.models import Course, Topic, Announcement


class UserRegistration(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'description', 'image')


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'


class AnnouncementForm(ModelForm):
    class Meta:
        model = Announcement
        fields = '__all__'