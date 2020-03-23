from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from .models import *
from .views import index, imprint

urlpatterns = [
    path('', index, name='index'),
    path('imprint/', imprint, name='imprint'),
]
