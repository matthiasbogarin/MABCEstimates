from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.forms.models import model_to_dict
import json
from .models import *
from datetime import datetime
import distutils.util
import os, calendar, requests, pdfkit, base64, uuid

pdfOptions = {
    'orientation': 'landscape',
    'page-size': 'A4',
    'margin-top': '0.5in',
    'margin-right': '0.5in',
    'margin-bottom': '0.5in',
    'margin-left': '0.5in',
    'encoding': "UTF-8",
    'zoom':'.9',
    'enable-local-file-access': ""
}

import pprint
pp = pprint.PrettyPrinter()

def index(request):
    context = {
        'all_files': Estimates.objects.all(),
    }
    return render(request, 'estimate_creator/creator.html', context)

def base64EncodeIOFile(ioFilePath:str) -> str:
    """
    function to read pdf file and convert binary to base64
    returns base64 bytes of pdf
    """
    with open(ioFilePath, "rb") as pdf_file:
        return base64.b64encode(pdf_file.read()).decode('utf-8')