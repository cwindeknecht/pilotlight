from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Show


def index(request):
    return HttpResponse("Hello World")


def calendar(request):
    next_seven_shows = Show.objects.order_by('date')[:7]
    context = {'next_seven_shows': next_seven_shows}
    return render(request, 'pilot/calendar.html', context)


def show(request, show_id):
    show = get_object_or_404(Show, pk=show_id)
    return render(request, 'pilot/show.html', {'show': show})


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
