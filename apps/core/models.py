from django.db import models

# Create your models here.
from django.db import models

class SiteInfo(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название сайта")
    description = models.TextField(verbose_name="Краткое описание")
    logo = models.ImageField(upload_to='logos/', verbose_name="Логотип сайта", blank=True, null=True)
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Электронная почта")
    address = models.CharField(max_length=255, verbose_name="Физический адрес")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Информация о сайте"
        verbose_name_plural = "Информация о сайте"