from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from .models import *
from .views import index

urlpatterns = [
    path('', login_required(index), name='index'),
]
