#criando um form em django
from django.forms import ModelForm
from .models import Produto

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao', 'marca', 'preco', 'categoria']
