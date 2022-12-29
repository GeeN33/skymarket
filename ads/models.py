from django.db import models

from users.models import User


class Ad(models.Model):

    title = models.CharField(max_length=150, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Пользователь', blank=False, null=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class Comment(models.Model):
    text = models.CharField(max_length=2000, blank=False)
    author =  models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Пользователь', null=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name = 'Объявление', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "комментарий"

    class Meta:
        verbose_name = "комментарий"
        verbose_name_plural = "комментарии"

