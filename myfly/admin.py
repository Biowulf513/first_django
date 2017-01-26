from django.contrib import admin
from .models import PlaneModel, PlaneStock


def plan_display_name(obj):
    return ("%s | %s летавший %s раз" % (obj.planModel, obj.reg_numb,
                                         obj.fly_col,))
plan_display_name.short_description = 'Наиминование'


def plan_bought(obj):
    return ("перобретён %s" % (obj.purchase,))
plan_bought.short_description = 'Дата преобретения'


class StockAdmin(admin.ModelAdmin):
    date_hierarchy = ('purchase')
    list_display = (plan_display_name, plan_bought)




class ModelAdmin(admin.ModelAdmin):
    list_display = ('model', 'style', 'seat', 'manufacture',)


admin.site.register(PlaneModel, ModelAdmin,)
admin.site.register(PlaneStock, StockAdmin,)
