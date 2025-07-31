from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    """
    Form for creating and updating tasks.
    """
    
    class Meta:
        model = Task
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task title...',
                'maxlength': 200,
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task description (optional)...',
                'rows': 4,
            }),
        }
        help_texts = {
            'title': 'Brief title for your task (required)',
            'description': 'Detailed description of your task (optional)',
        }

