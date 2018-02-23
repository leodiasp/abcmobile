# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect,get_object_or_404, render_to_response # funcoes de renderizacao dos templates
from django.contrib.auth import authenticate,login,logout
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime

from portal.models import *
from portal.forms import *

from mobile.models import *

from django.db.models import Sum, Avg, FloatField, Count

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import render

def mobile(request):

    return render(request, 'dashboard.html')