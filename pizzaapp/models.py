from django.db import models
from django.urls import reverse

class Category(models.Model):
    """ category model """
    name = models.CharField(max_length=255, blank=False, null=False, unique=True, error_messages={"unique":"Bu name alloqachon mavjud"})
    slug = models.CharField(max_length=255, blank=False, null=True, error_messages={"unique":"Bu slug alloqachon mavjud"})

    def get_absolute_url(self):
        return reverse('myapp:pizza_list_by_category', args=[self.slug])

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"

    def __str__(self):
        for_admin = f"{self.name} {self.slug}"
        return for_admin
    

class Pizza(models.Model):
    """ pizza model """
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.CharField(max_length=255, blank=False, null=True, error_messages={"unique":"Bu slug alloqachon mavjud"})
    image = models.ImageField(upload_to="Pizza/")
    updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('myapp:pizza_detail', args=[self.id, self.slug])
    
    class Meta:
        verbose_name = 'Pizza'
        verbose_name_plural = 'Pizza'

    def __str__(self):
        for_admin = f"{self.title} {self.slug} {self.price}"
        return for_admin


class pizzaNumbers(models.Model):
    branches = models.PositiveIntegerField(default=1)
    awards = models.PositiveIntegerField(default=1)
    customer = models.PositiveIntegerField(default=1)
    stuff = models.PositiveIntegerField(default=1)
    updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Pizza numbers'
        verbose_name_plural = 'Pizza numbers'

    def __str__(self):
        for_admin = f"{self.branches} {self.awards}"
        return for_admin


class Chef(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    specialist = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to="chefs/")
    updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Chef'
        verbose_name_plural = 'Chef'

    def __str__(self):
        for_admin = f"{self.first_name} {self.specialist}"
        return for_admin
    
    def get_full_name(self):
        return self.first_name + " " + self.last_name
    
