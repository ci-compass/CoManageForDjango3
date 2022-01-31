from django.shortcuts import render
from .models import MacAddr
from dataclasses import dataclass

def registration_view(request):
    query_dict = request.GET
    addressToAdd = query_dict.get("addr")
    context = {
        "addressToAdd" : addressToAdd,
        }
    obj = MacAddr()
    obj.username="NotYet."
    obj.address = addressToAdd
    obj.save()
    return render(request, "registration-view.html", context=context)

