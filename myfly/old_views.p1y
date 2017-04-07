from django.shortcuts import render, HttpResponse, get_object_or_404, get_list_or_404, render_to_response 
from django.views.generic import View
from .models import Route
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def table(request):
    routes_list = get_list_or_404(Route)

    paginator = Paginator(routes_list, 10)

    page = request.GET.get('page')

    try:
        routes = paginator.page(page)
    except PageNotAnInteger:
        routes = paginator.page(1)
    except EmptyPage:
        routes = paginator.page(paginator.num_pages)

    context = {'routes': routes}
    return render(request, 'myfly/table.html', context)


def flight(request, route_id):

    route = get_object_or_404(Route, pk=route_id)
    return render(request, 'myfly/flight.html', {'route': route})