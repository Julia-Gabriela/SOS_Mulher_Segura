from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class Usuario(models.Model):
    cpf = models.CharField(max_length=14, primary_key=True)
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=128)

    def set_password(self, raw_password):
       
        self.senha = make_password(raw_password)

    def check_password(self, raw_password):
       
        return check_password(raw_password, self.senha)

    def __str__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'usuarios'  
