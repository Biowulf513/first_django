from django.contrib import admin

from .models import Plane

admin.site.register(Plane)

from .models import PlaneRep

admin.site.register(PlaneRep)