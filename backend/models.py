from django.db import models

class Historico(models.Model):
    servidor = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    script = models.CharField(max_length=50)
    terminal = models.CharField(max_length=5000)
    data = models.DateTimeField()
    error = models.CharField(max_length=5000)


    def __str__(self):
        return self.usuario