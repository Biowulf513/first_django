from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import Route


class TableView(generic.ListView):
    model = Route
    template_name = 'myfly/table.html'
    context_object_name = 'routes_list'

    # def get_tableset(self):
    """Отображение списка всех рейсов"""
    #     return Route.objects.order_by('number')[:5]
    def get_tableset(self): 
        paginator = Paginator(TableView, 10)
        page = request.GET.get('page')

        try:
            routes = paginator.page(page)
        except PageNotAnInteger:
            routes = paginator.page(1)
        except EmptyPage:
            routes = paginator.page(paginator.num_pages)
        return routes



class FlightView(generic.DetailView):
    model = Route
    template_name = 'myfly/flight.html'