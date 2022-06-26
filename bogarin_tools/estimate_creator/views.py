from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.forms.models import model_to_dict
import json
from .models import *
from datetime import datetime
import distutils
import distutils.util
import csv
import io

import pprint
pp = pprint.PrettyPrinter()

def index(request):
    context = {
        'all_files': Estimates.objects.all(),
    }
    return render(request, 'estimate_creator/creator.html', context)