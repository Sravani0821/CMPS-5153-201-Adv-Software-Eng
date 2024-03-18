from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class SellerModel(models.Model):
    slug = models.SlugField(max_length=255, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name + "-" + self.last_name)
        super(SellerModel, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        db_table = "seller"
        verbose_name = "Seller"
        verbose_name_plural = "Sellers"
        ordering = ["first_name", "last_name"]
