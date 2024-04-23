from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) # Means that if user is deleted delete the profile but not vice versa i.e. when the profile is deleted not delete the user
    image = models.ImageField(default="default.jpg",upload_to="profile_pics")
    bio = models.CharField(max_length=250,default="A veteran of this application")
    
    def __str__(self) -> str:
        return f"Profile of -> {self.user.username}."
    
    def save(self) -> None: # for adding our own save method for this class (my goal is to automatically resize the images)
        super().save()  # there exist a save method in the superior class also we want that to first run then our one

        img = Image.open(self.image.path) # open the image that you want to resize

        if img.width != 250 or img.height != 250:
            output_size = 250,250
            img.thumbnail(output_size)
            img.save(self.image.path)



