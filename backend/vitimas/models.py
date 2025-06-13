from django.db import models
import datetime

class Vitima(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, default='000.000.000-00')  # default para evitar erro na migração
    email = models.EmailField(default='', blank=True)
    data_nascimento = models.DateField(default='2000-01-01')  # default para evitar erro na migração
    telefone = models.CharField(max_length=20, default='00000000000')  # adicionando default para evitar erro
    cep = models.CharField(max_length=9, default='00000-000')    
    bairro = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=10, default='0')  # default para evitar erro na migração
    complemento = models.CharField(max_length=100, blank=True, null=True)
    senha = models.CharField(max_length=128, default='senha123')  # default para evitar erro na migração

    def __str__(self):
        return self.nome
