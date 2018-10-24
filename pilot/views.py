from django.shortcuts import render
from django.http import HttpResponse

from .models import Show

def index(request):
    last_seven_days = Show.objects.order_by('-date')[:7]
    output = '***'.join([str(i) for i in last_seven_days])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
