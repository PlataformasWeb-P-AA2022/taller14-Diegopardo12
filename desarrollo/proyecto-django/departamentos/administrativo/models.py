from django.db import models

# Create your models here.

class Propietario(models.Model):
    opc_tipo_nacionalidad =(
        ('(Ecuatoriana)','Ecuatoriana'),
        ('(Peruana)','Peruana'),
        ('(Colombiana)','Colombiana')
        )

    nombre = models.CharField('Nombre',max_length=30)
    apellido = models.CharField('Apellido',max_length=30)
    edad = models.IntegerField('Edad')
    nacionalidad = models.CharField('Apellido',max_length=30,choices=opc_tipo_nacionalidad)

    def __str__(self):
        return "%s %s %d %s" % (self.nombre,
                self.apellido,
                self.edad,
                self.nacionalidad)

class Departamento(models.Model):
    
    costo_dep = models.DecimalField(max_digits=100, decimal_places=2)
    num_cuartos = models.IntegerField()
    num_banos = models.IntegerField()
    valor_ali = models.DecimalField(max_digits=100, decimal_places=2)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE,
            related_name="departamentos")

    def __str__(self):
        return "%d %d %d %d" % (
                self.costo_dep, 
                self.num_cuartos,
                self.num_banos,
                self.valor_ali)