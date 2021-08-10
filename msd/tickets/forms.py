from django import forms
from .models import Tickets


class TicketForm(forms.ModelForm):
    class Meta:
        model = Tickets
        # fields = '__all__'
        fields = ['title', 'content', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }