from django.db import models


class PlaneType(models.Model):

    class Meta:
        verbose_name = ('модель самолёта')
        verbose_name_plural = ('модели самолётов')

    choices_style = (
        (1, 'Пассажирский'),
        (2, 'Чартерный'),
        (3, 'Почтовый'),
        (4, 'Военный'),
    )

    name = models.CharField('Модель', max_length=20)
    style = models.PositiveSmallIntegerField(
        'Тип', choices=choices_style)
    seat = models.PositiveSmallIntegerField(
        'Кол-во мест', null=True, blank=True)
    manufacture = models.DateField('Дата выпуска')

    def __str__(self):
        return (self.name)


class Plane(models.Model):

    class Meta:
        verbose_name = ('самолёт в ангаре')
        verbose_name_plural = ('самолёты в ангаре')

    plane_type = models.ForeignKey(
        PlaneType, verbose_name='Модель самолёта', blank=True, null=True,
        on_delete=models.SET_NULL)
    purchase = models.DateField('Дата покупки')
    reg_numb = models.CharField('Рег. номер', max_length=6, unique=True)
    last_refit = models.DateField('Последний осмотр', null=True,
                                  blank=True)
    fly_col = models.PositiveSmallIntegerField('Кол-во полётов', null=True,
                                               blank=True)

    def __str__(self):
        return ((self.plane_type.name) + ' | ' + (self.reg_numb))


class Route(models.Model):

    class Meta:
        verbose_name = ('маршрут')
        verbose_name_plural = ('маршруты')

    name = models.CharField('Название', max_length=30,)
    number = models.CharField('Номер', max_length=6, unique=True)
    plane = models.ForeignKey('Plane', blank=True, null=True,
                              on_delete=models.SET_NULL,
                              verbose_name='Самолёт', )
    time = models.DateTimeField('Время вылета', )
    airport_out = models.ForeignKey('Airport', on_delete=models.CASCADE,
                                    related_name='outcoming_roures',
                                    verbose_name='Место вылета',)
    airport_in = models.ForeignKey('Airport', on_delete=models.CASCADE,
                                   related_name='incoming_roures',
                                   verbose_name='Место назначения',)

    def __str__(self):
        return (self.name)


class Airport(models.Model):

    class Meta:
        verbose_name = ('аэропорт')
        verbose_name_plural = ('аэропорты')

    name = models.CharField('Название', max_length=20,)
    code = models.CharField('Международный код', max_length=4,
                            null=True, blank=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE,
                             verbose_name='Город',)
    international = models.BooleanField('Интернационален', default=True,)

    def __str__(self):
        text = (str(self.name) + ' ✈ ' + str(self.city) + ' | ' +
                str(self.city.country))
        if self.international:
            text += ' | ⇔'
        else:
            text += ' | ⇎'

        return text


class City(models.Model):

    class Meta:
        verbose_name = ('город')
        verbose_name_plural = ('города')

    name = models.CharField('Название', max_length=20,)
    country = models.ForeignKey('Country', on_delete=models.CASCADE,
                                verbose_name='Страна',)

    def __str__(self):
        return (self.name)


class Country(models.Model):

    class Meta:
        verbose_name = ('страна')
        verbose_name_plural = ('страны')

    name = models.CharField('Название', max_length=20, unique=True)

    def __str__(self):
        return self.name
