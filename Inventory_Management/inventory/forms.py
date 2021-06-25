from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from rest_framework import serializers

#log in er jonno eirokom form nai.

class NewUserForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model = User
        fields = '__all__'
