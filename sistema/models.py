from django.db import models
from django.utils import timezone 

class Usuario(models.Model):
    nome = models.CharField(max_length = 50)
    sobrenome = models.CharField(max_length = 50)
    cpf = models.CharField(max_length = 20)
    telefone = models.CharField(max_length = 20)
    email = models.EmailField()
    endereco = models.CharField(max_length = 100)
    data_cadastro = models.DateTimeField(default = timezone.now)
    ativo = models.BooleanField(default = True)
    imagem = models.ImageField(blank=True, upload_to='Imagens/%Y/%m')

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    
class Genero(models.Model):
    nome = models.CharField(max_length = 50)
    data_cadastro = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return self.nome 

class Filme(models.Model):
    nome = models.CharField(max_length = 50)
    ano = models.DateField(default= timezone.now)
    estudio = models.CharField(max_length = 100)
    # genero = models.CharField(max_length = 70)
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True, blank=True)
    sinopse = models.TextField(max_length = 200)
    data_cadastro = models.DateTimeField(default = timezone.now)
     
     
    def __str__(self):
     return self.nome
     



    
    





