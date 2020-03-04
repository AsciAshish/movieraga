import json
import os

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, JsonResponse
from django.middleware import csrf
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from .models import *


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)
