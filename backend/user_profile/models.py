from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Avg
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
    rating_average = models.FloatField(default=0)
    review_count = models.IntegerField(default=0)
    tags = TaggableManager()

    def __str__(self):
        return self.name

    def update_review_fields(self):
        reviews = self.comments.all()
        #reviews = Review.objects.filter(id=self.id)
        self.rating_average = reviews.aggregate(models.Avg('rating')).get('rating__avg')
        self.review_count = reviews.count()
        self.save(update_fields=['rating_average', 'review_count'])

class Review(models.Model):
    publishTime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    isAnonymous = models.BooleanField(default=False)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    belongedResidence = models.ForeignKey(Residence, related_name='comments', on_delete=models.CASCADE)
    rating = models.FloatField(default=0)

    class Meta:
        ordering = ['publishTime']
    
    def __str__(self):
        # return super().__str__()
            return '%s - %s' % (self.belongedResidence.name, self.reviewer)
    
    def save(self, *args, **kwargs):
        super(Review, self).save(*args, **kwargs)
        self.belongedResidence.update_review_fields()
     