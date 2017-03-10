from django.shortcuts import render, HttpResponse, render_to_response
from django.views.generic import View
from .models import Route
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def table(request):
    routes_list = Route.objects.all()

    paginator = Paginator(routes_list, 10)

    page = request.GET.get('page')

    try:
        routes = paginator.page(page)
    except PageNotAnInteger:
        routes = paginator.page(1)
    except EmptyPage:
        routes = paginator.page(paginator.num_pages)

    return render(request, 'myfly/table.html', {'routes': routes})


def flight(request):
    if 'num' in request.GET and request.GET['num']:
        flight_num = request.GET['num']
        flight_info = Route.objects.filter(id=flight_num)
        return render_to_response('myfly/flight.html',
            {'flight_info': flight_info})
    else:
        return HttpResponseNotFound('<h1>Рейс не найден</h1>')
