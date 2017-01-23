from django.db import models

class Plane(models.Model):
    class Meta:
        verbose_name = "Самолёт"
        verbose_name_plural = "Все самолёты"

    model_name = models.CharField("Модель", max_length=20,)
    reg_number = models.CharField("Серийный номер", max_length=7,)

    def __str__(self):
        return str(self.model_name) + ' | ' + str(self.reg_number)

class PlaneRep(models.Model):
    class Meta:
        verbose_name = "Тип самолёта"
        verbose_name_plural = "Типы самолётов"

    fly_choices = (
            (1, 'Почтовый'),
            (2, 'Чартерный'),
            (3, 'Пассажирский'),
            (4, 'Частный'),
        )

    type_plane = models.PositiveSmallIntegerField("Тип", choices=fly_choices,)
    plane = models.ForeignKey(Plane, verbose_name = "Модель")
    seats_col = models.IntegerField("Кол-во мест", blank=True, null=True)
    old = models.DateField("Выпуск", )
    fly_sum = models.IntegerField("Кол-во перелётов", blank=True, null=True)
    last_fix = models.DateField("Последнее ТО", blank=True, null=True)
    funcioning = models.BooleanField("В эксплуатации", default=True)

    def __str__(self):
        return str(self.plane.model_name) + ' | ' + str(self.plane.reg_number)