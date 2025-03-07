from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    # resizing images
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if os.path.exists(self.avatar.path):
            img = Image.open(self.avatar.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.avatar.path)
