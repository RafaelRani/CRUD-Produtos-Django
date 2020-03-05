from django.db import models

class Produto(models.Model):
    CATEGORIA_CHOICES = (
            (1, "Importados"),
            (2, "Vestuário"),
            (3, "Acessórios"),
            (4, "Eletrodomésticos")
        )
    descricao = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.IntegerField(choices=CATEGORIA_CHOICES, default=1)

    def __str__(self):
        return self.descricao