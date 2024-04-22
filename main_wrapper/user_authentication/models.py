from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) # Means that if user is deleted delete the profile but not vice versa i.e. when the profile is deleted not delete the user
    image = models.ImageField(default=("default.jpg","default.png","default.jpeg"),upload_to="profile_pics")
    bio = models.CharField(max_length=250)
    
    def __str__(self) -> str:
        return f"Profile of {self.user.username}"