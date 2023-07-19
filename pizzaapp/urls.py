from django.urls import path
from pizzaapp import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('send/', views.send_mail, name='send_mail'),
    
    path("<slug:category_slug>/", views.pizza_list, name='pizza_list_by_category'),
    path('<int:id>/<slug:slug>/', views.pizza_detail, name='pizza_detail')
]
