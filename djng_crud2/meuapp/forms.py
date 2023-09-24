# meuapp/forms.py
from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'campo1': forms.TextInput(attrs={'class': 'border-2 border-red-600'}),
            'campo2': forms.TextInput(attrs={'class': 'border-2 border-red-600'}),
            # Adicione atributos de classe personalizados para outros campos conforme necessário
        }