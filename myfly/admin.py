from django.contrib import admin

from .models import PlaneModel

admin.site.register(PlaneModel)

from .models import PlaneStock

admin.site.register(PlaneStock)