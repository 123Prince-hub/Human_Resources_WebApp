from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Home, name="home"),
    path("opportunities/", Opportunities, name="opportunities"),
]
