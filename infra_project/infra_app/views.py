from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось!')


def second_page(request):
    return HttpResponse('SECRET PAGE')
