# Importing libraries.
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Defining biddermodel class
class BidderModel(models.Model):
    # fields
    slug = models.SlugField(max_length=255, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

# generate a slug based on first and last name.
    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name + "-" + self.last_name)
        super(BidderModel, self).save(*args, **kwargs)
# Unicode representation.
    def __unicode__(self):
        return self.first_name + " " + self.last_name
# String representation.
    def __str__(self):
        return self.first_name + " " + self.last_name
# Meta class for specifying metadata options for the model. 
    class Meta:
    
        db_table = "bidder"
        verbose_name = "Bidder"
        verbose_name_plural = "Bidders"
        ordering = ["first_name", "last_name"]
