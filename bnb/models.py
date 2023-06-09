from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.conf import settings
from datetime import date


class Customer(models.Model):
    """
    CUSTOMER CONTACT FORM, allows site
    visitors to write a message or query to
    the business owners.
    """
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField()
    message = models.TextField(max_length=350, blank=True)

    def __str__(self):
        return str(self.title)


class Menu(models.Model):
    """
    ADD MENU ITEM as Admin user through Django
    """
    category = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=350)

    def __str__(self):
        return self.name


class Item(models.Model):
    """
    MENU ITEM CATEGORIES
    """
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True, unique=True)
    description = models.TextField(max_length=250)

    MEAT = "Meat"
    SAVORY_BREADS = "Bread"
    PASTRIES = "Pastry"
    FRESH_FRUIT = "Fruit"
    VEGAN_OPTIONS = "Vegan"
    DRINKS = "Drinks"

    FOOD_TYPE = [
        (MEAT, "Meat"),
        (SAVORY_BREADS, "Bread"),
        (PASTRIES, "Pastry"),
        (FRESH_FRUIT, "Fruit"),
        (VEGAN_OPTIONS, 'Vegan'),
        (DRINKS, 'Drinks'),
    ]
    food_type = models.CharField(
        ('food_type'),
        max_length=25,
        choices=FOOD_TYPE,
        default="Meat"
        )

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


class MenuItem(models.Model):
    """
    ADD NEW CATEGORY TO DJANGO DATABASE
    """
    item_name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=300, blank=True)


class Room(models.Model):
    """
    BOOK A ROOM
    """
    ROOM_CATEGORIES = (
        ('Master Bedroom', 'Master Bedroom'),
        ('Queen Bedroom', 'Queen Bedroom'),
    )

    category = models.CharField(max_length=50, choices=ROOM_CATEGORIES, blank=True, null=True)  # noqa
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.category}.'


class Booking(models.Model):
    """
    BOOKING ROOMS. Model uses the User Foreign Key
    so each booking is associated with a user.
    User is authenticated but doesn't have to be Admin.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField(null=False, default=date(2023, 5, 21))
    check_out = models.DateField(null=False, default=date(2023, 5, 28))
