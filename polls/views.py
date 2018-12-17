# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def hiddenpoll(request):
    return HttpResponse("Welcome to the hidden poll!")
