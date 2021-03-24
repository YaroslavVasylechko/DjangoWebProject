from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anouncement', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title of article or news'
            }),
            'anouncement': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'anouncement'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'date'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text of artticle'
            })

        }