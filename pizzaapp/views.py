from django.shortcuts import render, get_object_or_404
from pizzaapp.models import Category, Pizza, pizzaNumbers, Chef
from config.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage
from django.http import HttpResponse

def home(requests):
    pizzaNumberss = pizzaNumbers.objects.all()
    pizza = Pizza.objects.filter(category__slug='pizza')[:6]
    categories = Category.objects.all()
    context = {
        'pizza':pizza,
        'categories':categories,
        "pizzaNumberss":pizzaNumberss
    }

    return render(requests, "index.html", context)

def menu(requests):
    categories = Category.objects.all()
    pizza = Pizza.objects.filter(category__slug='pizza')[:8]
    context = {
        'pizza':pizza,
        "categories":categories
    }

    return render(requests, "menu.html", context)

def services(requests):
    pizza = Pizza.objects.filter(category__slug='pizza')[:8]
    context = {
        "pizza":pizza
    }
    return render(requests, "services.html", context)

def about(requests):
    chefs = Chef.objects.all().order_by('-id')[:4]
    context = {
        "chefs":chefs
    }

    return render(requests, "about.html", context)

def contact(requests):
    return render(requests, "contact.html")


def pizza_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    pizza = Pizza.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        pizza = pizza.filter(category=category)

        context = {
           "category":category,
           "categories":categories,
           "pizza":pizza
        }
        return render(request, 'index.html', context)  

def pizza_detail(request, id, slug):
    pizza = get_object_or_404(Pizza, id=id, slug=slug)

    context =  {
        "pizza":"pizza"
    } 

    return render(request, "pizza_detail.html", context)


def send_mail(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        gmail = EmailMessage(
            f"Subject: {name}",
            f"Mahsulot nomi: {subject}\n\n Elektron pochta: {email}\n\n Xabar: {message}",
            email,
            [EMAIL_HOST_USER],
        )
        gmail.send(fail_silently = True)
    return render(request, "contact.html", {"name":name})
