from django.contrib import admin
from django.utils.html import mark_safe
from Site.models import Cliente, Departamento, Produto

# Register your models here.
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    list_display_links = ['id', 'nome']

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'preco', 'avaliacao', 'departamento', 'ver_imagem']
    list_display_links = ['id', 'nome']
    list_filter = ['departamento']
    readonly_fields = ['ver_imagem']

    def ver_imagem(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.imagem.url,
            width=75,
            height=75,
            )
    )

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'cidade', 'uf']
    list_display_links = ['id', 'nome']
    list_filter = ['bairro', 'cidade']
    search_fields = ['nome']

admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Produto, ProdutoAdmin)    
admin.site.register(Cliente, ClienteAdmin)
