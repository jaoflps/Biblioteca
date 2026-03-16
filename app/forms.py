from django import forms
from .models import Livro
# Importações necessárias para o FormHelper funcionar
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(LivroForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'titulo',      # Antes estava 'titulo'
            'autor',
            'editora',
            'genero',
            'preco',
            'data_pub', # Antes estava 'data_pub'
            'status',
            Submit('submit', 'Salvar', css_class='btn-success')
        )