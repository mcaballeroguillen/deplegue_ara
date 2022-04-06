from django.db import  models

class Line_Presupuesto(models.Model):
    Proyecto = models.CharField(max_length=150)
    Id = models.IntegerField(primary_key=True)
    Codigo= models.CharField(max_length=500)
    Total = models.FloatField()
    Ejecutado = models.FloatField()
    En_Ejucucion = models.FloatField()
    Saldo = models.FloatField()

    def __str__(self):
        return  self.Codigo
    class Meta:
        unique_together = ['Proyecto', 'Codigo']

class Cronogram(models.Model):
    Proyecto = models.CharField(max_length=150)
    Archivo_excel = models.FileField(upload_to='calendarapp/excel/')

    def __str__(self):
        return self.Proyecto
