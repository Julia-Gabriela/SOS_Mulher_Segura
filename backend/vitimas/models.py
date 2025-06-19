from django.db import models


class Usuario(models.Model):
    cpf = models.CharField(max_length=14, primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    senha = models.CharField(max_length=128)
    telefone = models.CharField(max_length=11)
    data_nascimento = models.DateField(null=True, blank=True)
    data_cadastro = models.DateField(auto_now_add=True)
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        managed = False  # Django não cria nem altera essa tabela
        db_table = 'usuarios'  # Nome da tabela no banco

    def __str__(self):
        return self.nome
