from django.contrib import admin
from django.urls import path

from zgloszenia.views import dodaj_zgloszenie


urlpatterns = [
    path("", dodaj_zgloszenie, name="dodaj_zgloszenie"),
    path("admin/", admin.site.urls),
]