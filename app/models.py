from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class Tecnologia(models.Model):
    nome = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.nome

class Post(models.Model):
    titulo = models.CharField(max_length=300,null=False,blank=False)
    descricao = models.CharField(max_length=500,null=False,blank=False)
    conteudo = models.TextField(null=False,blank=False)
    autor = models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)
    tecnologias = models.ManyToManyField(Tecnologia,blank=False)

    def __str__(self):
        return f"Titulo:{self.titulo} - Descrição:{self.descricao}, Escrito por:{self.autor}"

    def get_absolute_url(self):
        return reverse('lista_post',args=[str(self.id)])
