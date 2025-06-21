from django.db import models
from vitimas.models import Usuario

class Denuncia(models.Model):
    id_denuncia = models.AutoField(primary_key=True)
    cpf = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        db_column='cpf'
    )
    descricao = models.TextField(null=False, blank=False)
    data_hora = models.DateTimeField(null=False)
    localizacao = models.CharField(max_length=255, null=False, blank=False)
    provas_anexadas = models.BooleanField(default=False)
    arquivo = models.CharField(max_length=255, blank=True, null=True)  # Caminho do arquivo

    class Meta:
        managed = True
        db_table = 'denuncias'  # ✅ Removi managed=False

    def __str__(self):
        return f"Denúncia {self.id_denuncia} - {self.cpf}"
