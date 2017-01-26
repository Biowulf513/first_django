from django.contrib import admin

from .models import PlaneType, Plane


def plane_display_name(obj):
    return ("%s | %s летавший %s раз" % (obj.planeType, obj.reg_numb,
                                         obj.fly_col,))
plane_display_name.short_description = 'Наиминование'


def plan_bought(obj):
    return ("перобретён %s" % (obj.purchase,))
plan_bought.short_description = 'Дата преобретения'


class PlaneAdmin(admin.ModelAdmin):
    date_hierarchy = ('purchase')
    list_display = (plane_display_name, plan_bought,)


class PlaneTypeAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'style', 'seat', 'manufacture',)

admin.site.register(PlaneType, PlaneTypeAdmin,)
admin.site.register(Plane, PlaneAdmin,)