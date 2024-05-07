from django.http import HttpResponse
from django.shortcuts import render
from .task import test_func
from send_mail_app.task import send_mail_func

def test(request):
    test_func.delay()
    return HttpResponse('view done')

def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("celery mail send")

