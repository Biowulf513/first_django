from django.shortcuts import render
# from django.utils import timezone

from .models import Route

def all(request):
	routes = Route.objects.all()
	return render(request, 'myfly/table.html', {'routes': routes})

# def number(request, number_id):
# 	# return HttpResponse('твой номер %s' % number_id)
# 	return render(request, 'blog/.html')