from django.contrib import admin
from contatos.models import Contato
admin.site.register(Contato)

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'telefone', 'email')
    list_display_links = ('id', 'nome')
    search_fields= ('id', 'nome')



# Register your models here.
