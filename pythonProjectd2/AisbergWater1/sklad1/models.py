from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('material_warehouse_manager', 'Начальник склада материалов'),
        ('finished_goods_warehouse_manager', 'Начальник склада готовой продукции'),
        ('sales_director', 'Директор по продажам'),
    )
    role = models.CharField(max_length=40, choices=ROLE_CHOICES)