from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager

# Create your models here.


class User(AbstractUser):
    isVerifiedUser = models.BooleanField(default=False)
    isResidenceManager = models.BooleanField(default=False)


class Location(models.Model):
    streetName = models.CharField(max_length=100)
    streetNum = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=6)


class Residence(models.Model):
    name = models.CharField(max_length=100)
    manager = models.ManyToManyField(User)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return self.name


class Review(models.Model):
    publishTime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    isAnonymous = models.BooleanField(default=False)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    belongedResidence = models.ForeignKey(Residence, related_name = 'comments', on_delete=models.CASCADE)
    class Meta:
        ordering = ['publishTime']
    
    def __str__(self):
        # return super().__str__()
            return '%s - %s' % (self.belongedResidence.name, self.reviewer)
     