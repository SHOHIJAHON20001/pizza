from django.contrib import admin
from . models import Category, Pizza, pizzaNumbers, Chef
from django.contrib.auth.models import Group

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Category, CategoryAdmin)
admin.site.unregister(Group)

class PizzaAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "price", "created_at"]
    prepopulated_fields = {"slug": ("title",)}
    

admin.site.register(Pizza, PizzaAdmin)

class pizzaNumbersadmin(admin.ModelAdmin):
    list_display = ["branches", "awards", "customer", "stuff", "created_at"]

admin.site.register(pizzaNumbers, pizzaNumbersadmin)

class chefAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "specialist", "created_at"]

admin.site.register(Chef, chefAdmin)
