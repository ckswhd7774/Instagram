from django import forms
from social.models import Article

class ArticleForm(forms.ModelForm) :
    class Meta :
        model = Article
        fields = {'title', 'article', 'image'}