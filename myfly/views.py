from django.shortcuts import render
from .models import Route

def all(request):
	routes = Route.objects.all()
	return render(request, 'myfly/table.html', {'routes': routes})
