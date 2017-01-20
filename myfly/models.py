from django.db import models

class Plane(models.Model):
    model_name = models.CharField(max_length=20,)
    reg_number = models.CharField(max_length=7,)

    def __str__(self):
        return self.model_name

    def __str__(self):
        return str(self.model_name) + ' | ' + str(self.reg_number)

class PlaneRep(models.Model):
    fly_choices = (
        ('P', 'Post'),
        ('C', 'Charter fly'),
        ('PT', 'Passenger fly'),
        ('VIP', 'VIP fly'),
        )

    type_plane = models.CharField(max_length=20, choices=fly_choices, default='C')
    plane = models.ForeignKey(Plane)
    seats_col = models.DecimalField(max_digits=3,decimal_places=0,)
    old = models.IntegerField()
    fly_sum = models.IntegerField()
    last_fix = models.DateField()
    funcioning = models.BooleanField(default=True,)

    def __str__(self):
        return str(self.plane) + ' | ' + str(self.plane.reg_number)