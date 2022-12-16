from django import forms
from .models import Review, Category

choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'author', 'albumName', 'albumArtist', 'albumGenre', 'albumScore', 'category', 'body', 'albumArt')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id': 'elder', 'type': 'hidden'}),
            # 'author': forms.Select(choices = choice_list, attrs={'class': 'form-control', 'placeholder': 'Author'}),
            'albumName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Album Name'}),
            'albumArtist': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Artist'}),
            'albumGenre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Genre'}),
            'albumScore': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rating out of 10'}),
            'category': forms.Select(choices = choice_list, attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write Review Here' }),
        }
