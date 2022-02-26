from tabnanny import verbose
from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=50, null=False, blank=False, verbose_name='Descrição')

    def __str__(self) -> str:
        return self.descricao
    class Meta:
        verbose_name_plural = 'Categorias'

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    cnpj = models.CharField(max_length=20, verbose_name='CNPJ')
    contato_email = models.CharField(max_length=100, null=True, blank=True, verbose_name='Email')
    contato_telefone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Telefone')

    
    def __str__(self) -> str:
        return self.nome
    class Meta:
        verbose_name_plural = 'Fornecedores'

class Produto(models.Model):
    nome = models.CharField(max_length=30, verbose_name='Nome do produto')
    valor = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Valor')
    qte_estoque = models.IntegerField(verbose_name='Quantidade em estoque')
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')
    id_fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, verbose_name='Fornecedor')

    def __str__(self) -> str:
        return self.nome
    class Meta:
        verbose_name_plural = 'Produtos'