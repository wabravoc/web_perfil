from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from django.http import Http404
from collections import namedtuple
from colorama import init, Fore
from .models import user_contact

def index(request):
    TAG="[INDEX]"
    init(autoreset=True) 
    print(Fore.CYAN + TAG + "main views was open")
    return render(request, 'capstone/index.html')

# Create your views here.
def CD_PDF(request):
    TAG="[CV_PDF]"
    init(autoreset=True) 
    print(Fore.CYAN + TAG + "PDF views was open")
    return render(request, 'capstone/view_pdf.html')

@csrf_exempt
def register_user(request):
    
    TAG="[REGISTER]"
    init(autoreset=True) 
    
    print(Fore.GREEN + TAG + "add a new contact")
    
    if request.method != "POST":
        print(Fore.RED + TAG + 'Bad POST')
        return JsonResponse({"error": "POST request required."}, status=400)
    data = json.loads(request.body)
    
    New_contact=user_contact(
        first_name=data.get("f_name"),
        last_name=data.get("l_name"),
        celphone=data.get("cel"),
        email=data.get("email"),
        message=data.get("message"),
    )
    New_contact.save()
    print(Fore.CYAN + TAG + "New contact was saved")
    print(Fore.CYAN + TAG + "return Json response")
    return JsonResponse({"message": "publicated successfully."}, status=201)

    

        
        