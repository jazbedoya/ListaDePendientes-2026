from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'tipo', 'fecha_limite', 'completo']
        widgets = {
            'fecha_limite': forms.DateInput(
                attrs={'type': 'date'}
            )
        }
