from unicodedata import category
from django import forms
from .models import Category

class PostForm(forms.Form):
    category_deta = Category.objects.all()
    category_choice = {}
    for category in category_deta:
        category_choice[category] = category

    title = forms.CharField(max_length=30, label='タイトル')
    category = forms.ChoiceField(label='カテゴリ', widget=forms.Select, choices=list(category_choice.items()))
    content = forms.CharField(label='内容', widget=forms.Textarea())
    image = forms.ImageField(label='イメージ画像', required=False)