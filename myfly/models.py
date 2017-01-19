from django.db import models

class Plane(models.Model):
    model_name = models.CharField(max_length=20,)
    reg_number = models.CharField(max_length=7,)

    def __str__(self):
        return self.model_name

class PlaneRep(models.Model):
    type_plane = models.CharField(max_length=20,)
    plane = models.ForeignKey(Plane)
    seats_col = models.DecimalField(max_digits=3,decimal_places=0,)
    old = models.DecimalField(max_digits=2,decimal_places=0,)
    fly_sum = models.DecimalField(max_digits=5,decimal_places=0,)
    last_fix = models.DateField()
    funcioning = models.BooleanField(default=True,)

    def __str__(self):
        return str(self.plane) + ' | ' + str(self.plane.reg_number)