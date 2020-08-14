from django import forms
from django.forms import ModelForm
from. models import NewsStory


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content', 'image_url', 'author']
        widgets ={
            'pub_date': forms.DateInput(
                format=('%m/%d%Y'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date'
        
                }
            ),
            # 'title': forms.TextInput(
            #     attrs={
            #         'class':forms,
            #         'placeholder': 'Text Here',
            #     }
            # ),
            #  'content': forms.TextInput(
            #     attrs={
            #         'class':forms,
            #         'placeholder': 'Text Here',
            #     }
            # ),
            # 'author': forms.TextInput(
            #     attrs={
            #         'class': forms,
            #         'placeholder': 'Text Here',
            #     }
            # ),
            # 'button': forms.TextInput(
            #     attrs={
            #         'class':forms,
            #         'placeholder': 'Text Here',
            #     }
            # ),
        }