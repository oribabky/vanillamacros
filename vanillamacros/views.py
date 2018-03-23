from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('vanillamacros/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def wowClass(request, className):
    template = loader.get_template('vanillamacros/index.html')
    context = {
        'className': className,
    }
    return HttpResponse(template.render(context, request))

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)    