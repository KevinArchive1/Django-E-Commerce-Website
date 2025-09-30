from django.shortcuts import render
from .models import Shoes


# Create your views here.

def main(request):
    return render(request, "main.html")

def home(request):
    return render(request, 'home.html')

def shop(request):
    category = request.GET.get("category", "all")
    if category == "all":
        shoes = Shoes.objects.all()
    else:
        shoes = Shoes.objects.filter(category=category)

    return render(request, "shop.html", {"shoes": shoes, "selected_category": category})

def about(request):
    return render(request, "about.html")
