from django.contrib import admin

from .models import PlaneType, Plane, Route, Airport, City, Country


def plane_display_name(obj):
    return ("%s | %s летавший %s раз" % (obj.plane_type, obj.reg_numb,
                                         obj.fly_col,))
plane_display_name.short_description = 'Наиминование'


def plan_bought(obj):
    return ("перобретён %s" % (obj.purchase,))
plan_bought.short_description = 'Дата преобретения'


class PlaneAdmin(admin.ModelAdmin):
    date_hierarchy = ('purchase')
    list_display = (plane_display_name, plan_bought,)


class PlaneTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'style', 'seat', 'manufacture',)





admin.site.register(Route)
admin.site.register(PlaneType, PlaneTypeAdmin,)
admin.site.register(Plane, PlaneAdmin,)
admin.site.register(Airport)
admin.site.register(City)
admin.site.register(Country)