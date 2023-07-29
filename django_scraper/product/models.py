from django.db import models

class data(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=20)
    url = models.URLField()
    image_url = models.URLField()

    class Meta:
        verbose_name = 'Product Data'
        verbose_name_plural = 'Product Data'

    def __str__(self) -> str:
        return self.Name