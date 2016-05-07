from django.db import models
from django.utils import timezone


class   Women(models.Model):
    Yazar = models.ForeignKey('auth.User')
    Baslik = models.CharField(max_length=200)
    Yazi = models.TextField()
    Yazilma_Tarihi = models.DateTimeField(
            default=timezone.now)
    Yayinlama_Tarihi = models.DateTimeField(
            blank=True, null=True)

    def yayinla(self):
        self. Yayinlama_Tarihi = timezone.now()
        self.save()

    def __str__(self):
        return self.Baslik
