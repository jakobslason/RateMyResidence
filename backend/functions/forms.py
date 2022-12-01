from email.policy import default
from pickle import FALSE
from django import forms
from taggit.forms import *
from backend.user_profile.models import Review, Residence, Reply


class ResidenceForm(forms.Form):
    name = forms.CharField(label='Residence name', max_length=100)
    streetName = forms.CharField(max_length=100)
    streetNum = forms.CharField(max_length=20)
    zipcode = forms.CharField(max_length=6)
    university = forms.BooleanField(label = "university residence", initial=False, required=False)
    distance = forms.FloatField(min_value=0)
    parking_policy = forms.ChoiceField(label="Select a parking policy", choices=Residence.ParkingPolicy.choices)
    pet_policy = forms.ChoiceField(label="Select a pet policy", choices=Residence.PetPolicy.choices)
    residence_tags = TagField()
    image = forms.ImageField(label="Upload image for residence", required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))

class ResidenceEditForm(forms.Form):
    name = forms.CharField(label='Residence name', max_length=100)
    streetName = forms.CharField(max_length=100)
    streetNum = forms.CharField(max_length=20)
    zipcode = forms.CharField(max_length=6)
    university = forms.BooleanField(label = "university residence", initial=False, required=False)
    distance = forms.FloatField(min_value=0)
    website = forms.CharField(max_length=150)
    parking_policy = forms.ChoiceField(label="Select a parking policy", choices=Residence.ParkingPolicy.choices)
    pet_policy = forms.ChoiceField(label="Select a pet policy", choices=Residence.PetPolicy.choices)
    residence_tags = TagField()


class ReviewForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(max_length=500)
    isAnonymous = forms.BooleanField(label = "Post Anonymously?", initial=False, required=False)
    rating = forms.DecimalField(min_value=0, max_value=5)
    time_lived = forms.IntegerField(label= "How long have you been living in this residence (semester)?", required=False)
    live_again = forms.BooleanField(label= "Would you live in this residence again?", initial=False, required=False)
    rent = forms.IntegerField(label="How much are you paying for your residence a month?", required=False)
    location_rating = forms.DecimalField(min_value=0, max_value=5)
    quietness_rating = forms.DecimalField(min_value=0, max_value=5)
    quality_rating = forms.DecimalField(min_value=0, max_value=5)
    room_type = forms.ChoiceField(label="Select your room type", choices=Review.RoomType.choices)
    has_furniture = forms.BooleanField(label="Does this residence provide furniture", required=False)
    image = forms.ImageField(label="Upload images for your review", required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))


class EditReview(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(max_length=500)
    isAnonymous = forms.BooleanField(label = "Post Anonymously?", initial=False, required=False)
    rating = forms.DecimalField(min_value=0, max_value=5)
    time_lived = forms.IntegerField(label= "How long have you been living in this residence (semester)?", required=False)
    live_again = forms.BooleanField(label= "Would you live in this residence again?", initial=False, required=False)
    rent = forms.IntegerField(label="How much are you paying for your residence a month?", required=False)
    location_rating = forms.DecimalField(min_value=0, max_value=5)
    quietness_rating = forms.DecimalField(min_value=0, max_value=5)
    quality_rating = forms.DecimalField(min_value=0, max_value=5)
    room_type = forms.ChoiceField(label="Select your room type", choices=Review.RoomType.choices)
    has_furniture = forms.BooleanField(label="Does this residence provide furniture", required=False)


class DeleteReview(forms.Form):
    isDelete = forms.BooleanField(label="Delete post", initial=False, required=False)
    notDelete = forms.BooleanField(label = "Not delete post", initial=False, required=False)


class UpdateForm(forms.Form):
    room_type = forms.ChoiceField(label="Select your room type", choices=Review.RoomType.choices)


class ReviewPhotoForm(forms.Form):
    image = forms.ImageField()


class RequestForm(forms.Form):
    isApproved = forms.BooleanField(label='Approve the request?',  required=False)

class ReplyForm(forms.Form):
    content = forms.CharField(max_length=500)

class EditReply(forms.Form):
    content = forms.CharField(max_length=500)