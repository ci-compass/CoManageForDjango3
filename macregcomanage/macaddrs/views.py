from django.shortcuts import render
#from dataclasses import dataclass
from .models import MacAddr


# Create your views here.
def registration_view(request):
    query_dict = request.GET
    addressToAdd = query_dict.get("addr")
    context = {
        "addressToAdd" : addressToAdd,
        }
    user = request.user
    obj = MacAddr()
    obj.userEmail=user.email
    obj.macAddress = addressToAdd
    obj.save()
    return render(request, "registration-view.html", context=context)
