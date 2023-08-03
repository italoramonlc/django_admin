from django.db import models
from django.contrib import admin
from .models import Post,Tecnologia
from django.contrib.auth.models import User
from mdeditor.widgets import MDEditorWidget
# Register your models here.
admin.site.unregister(User)

class PostInline(admin.StackedInline): #ou pode usar o TabularInline
    model = Post
    extra = 1

class UserAdmin(admin.ModelAdmin):
    inlines = [PostInline,]


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {"widget":MDEditorWidget}
    }
    fieldsets = (
        (None,{# None aparece por padrão
            'fields':('titulo','descricao','conteudo')
        }),
         ('Relacionamentos',{# nesse caso está add nome a categoria
             'classes':('collapse',),# collapse mostrar show e hide button
             'fields':('autor','tecnologias')
         }),
        )
    list_display = ['descricao','titulo']
    list_filter = ['titulo',]
    list_per_page = 10
    search_fields = ['titulo']
    search_help_text = "Buscar de posts por titulo"
    view_on_site = True

admin.site.register(User,UserAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Tecnologia)


