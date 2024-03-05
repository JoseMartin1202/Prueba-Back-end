from django.db import models

class Tarea(models.Model):
    idTarea = models.AutoField(auto_created=True, primary_key=True)
    titulo = models.CharField(max_length=200, blank=False, null=False, default='nueva tarea')
    completada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo