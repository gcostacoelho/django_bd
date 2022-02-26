from django.contrib import admin
from core.models import Categoria, Fornecedor, Produto
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Fornecedor)
admin.site.register(Produto)