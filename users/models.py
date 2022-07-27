from django.db import models
from django.contrib.auth.models import User, Group
from PIL import Image


# Se usa OneToOne para que cada usuario se guarde individualmente
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
# Guardar la imagen
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()
    def __str__(self):
        return self.user.username

    # redimensionar imagen
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)