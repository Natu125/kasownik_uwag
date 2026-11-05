from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import FormularzZgloszenia


def dodaj_zgloszenie(request):
    if request.method == "POST":
        formularz = FormularzZgloszenia(request.POST)
        if formularz.is_valid():
            formularz.save()
            messages.success(request, "Dziękujemy! Twoje zgłoszenie zostało przyjęte.")
            return redirect("dodaj_zgloszenie")
    else:
        formularz = FormularzZgloszenia()

    return render(request, "zgloszenia/formularz.html", {"formularz": formularz})