from django.shortcuts import render
from .models import Route
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def all(request):
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
