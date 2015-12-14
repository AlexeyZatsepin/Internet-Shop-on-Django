from django.forms import ModelForm
from .models import Comment, Cart , Email
from django import forms


class CommentForm(ModelForm):
    class Meta():
        model = Comment
        fields = ['comment_text']


class CartForm(ModelForm):
    class Meta():
        model = Cart
        fields = ['quantity']


class OrderForm(ModelForm):
    class Meta():
        model = Email
        fields = ['email']
