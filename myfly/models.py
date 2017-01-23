from django.db import models


class PlaneModel(models.Model):

    class Meta:
        verbose_name = ("Модель самолёта")
        verbose_name_plural = ("Модели самолётов")

    choices_style = (
        (1, 'Пассажирский'),
        (2, 'Чартерный'),
        (3, 'Почтовый'),
        (4, 'Военный'),
    )

    model = models.CharField("Модель", max_length=20)
    style = models.PositiveSmallIntegerField(
        "Тип", choices=choices_style)
    seat = models.PositiveSmallIntegerField(
        "Кол-во мест", null=True, blank=True)
    reg_numb = models.CharField("Рег. номер", max_length=6)
    manufacture = models.DateField("Дата выпуска")

    def __str__(self):
        return ((self.model) + ' | ' + (self.reg_numb))


class PlaneStock(models.Model):

    class Meta:
        verbose_name = ("Самолёт в ангаре")
        verbose_name_plural = ("Самолёты в ангаре")

    planModel = models.ForeignKey(PlaneModel, on_delete=models.CASCADE)
    purchase = models.DateField("Дата покупки")
    last_refit = models.DateField(
        "Последний осмотр", null=True, blank=True)
    fly_col = models.PositiveSmallIntegerField(
        "Кол-во полётов", null=True, blank=True)

    def __str__(self):
        return ((self.planModel.model) + ' | ' + (self.planModel.reg_numb))