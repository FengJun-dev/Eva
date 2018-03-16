from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator


# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    sub_category = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return 'sub_category:"{sub_category}" category:"{category}"'.format(
            sub_category=self.sub_category,
            category=self.category,
        )


class Store(models.Model):
    id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=30, null=True)
    store_image = models.ImageField(default=None)

    def __str__(self):
        return self.store_name


class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=150, validators=[UnicodeUsernameValidator()])
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender_choices = (
        ('m', 'male'),
        ('f', 'female')
    )
    gender = models.CharField(max_length=2, choices=gender_choices)
    password = models.CharField(max_length=128, null=True, blank=True, default=None)

    @property
    def full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    def __str__(self):
        return 'id="{id}" email="{email}" name="{name}"'.format(
            id=self.id,
            email=self.email,
            name=self.full_name,
        )


class ShopItem(models.Model):
    id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=128)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    created = models.DateTimeField()
    like = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    region = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    stock_choices = (
        (1, 'in stock'),
        (2, 'not in stock'),
    )
    stock = models.IntegerField(choices=stock_choices)
    item_image = models.ImageField(default=None)

    def __str__(self):
        return 'id="{id}" item_name="{item_name}"'.format(
            id=self.id,
            item_name=self.item_name,
        )


class UserComment(models.Model):
    pass