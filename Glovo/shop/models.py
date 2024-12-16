from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(default=0)
    date_registered = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=25, null=True, blank=True)
    phone_number = models.PositiveSmallIntegerField(default=0)
    STATUS_CHOICES = (
        ('gold', 'gold'),
        ('silver', 'silver'),
        ('bronze', 'bronze'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='bronze')


class Category(models.Model):
    name = models.CharField(max_length=100)


class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    resto_name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='img/')
    price = models.IntegerField(default=0)


class Courier(models.Model):
    courier_name = models.CharField(max_length=100)
    phone_number = models.PositiveSmallIntegerField(default=0)
    STATUS_CHOICES = (
        ("машина", "машина"),
        ("мопед", "мопед"),
        ("велик", "велик"),
    )
    status = models.CharField(max_length=16, choices=STATUS_CHOICES)


class Order(models.Model):
    order_number = models.IntegerField(default=0)
    resto_name = models.ForeignKey(Food, on_delete=models.CASCADE)
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    delivery_time = models.DateTimeField()
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)


class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ("доставлено", "доставлено"),
        ("обрабатка", "обрабатка"),
        ("в пути", "в пути"),
    )
    status = models.CharField(max_length=16, choices=STATUS_CHOICES)


class Rating(models.Model):
    resto_name = models.ForeignKey(Food, on_delete=models.CASCADE)
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1,6)], verbose_name="Rating")


class Review(models.Model):
    author = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Сообщение", max_length=5000)
    movie = models.ForeignKey(Food, on_delete=models.CASCADE)
    parent_review = models.ForeignKey('self',  related_name='replies',  null=True, blank=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
