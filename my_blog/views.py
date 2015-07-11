from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import send_mail
from django import forms

# Create your views here.


def index(request):
    return render_to_response('my_blog/index.html', context_instance=RequestContext(request))
