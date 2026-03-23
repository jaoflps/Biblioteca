# Registre seus modelos aqui.
from django.contrib import admin
from .models import *


admin.site.register(Cidade)
# admin.site.register(Autor) 
admin.site.register(Editora)
admin.site.register(Leitor)
admin.site.register(Livro)
admin.site.register(Genero)
admin.site.register(Emprestimo)

# Os inlines vem primeiro, pois eles são usados dentro do admin do autor
class LivroInline(admin.TabularInline):
    model = Livro
    extra = 1

# Agora criamos a classe do admin do autor, onde vamos usar o inline para mostrar os livros relacionados a cada autor
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [LivroInline] # Isso faz os livros aparecerem dentro do autor


admin.site.register(Autor, AutorAdmin)