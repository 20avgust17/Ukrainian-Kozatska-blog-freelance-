from django import forms
from .models import Feedback


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ім'я"}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Пошта"}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Номер телефону"}),
            'content': forms.Textarea(
                attrs={'class': 'form-control', 'cols': 30, 'rows': 7, 'placeholder': "Повiдомлення"}),

        }
