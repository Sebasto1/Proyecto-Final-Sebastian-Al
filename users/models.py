from django.db import models
from django.contrib.auth.models import User, Group
from PIL import Image

# #class Admin(models.Model):
#     name = models.CharField(max_length=(20))
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     last_name = models.CharField(max_length=(20))
#     email = models.EmailField()
#     admin_group, created = Group.objects.get_or_create(name="Admin")
#     def __str__(self):
#         return f"Nombre: {self.name} - Apellido: {self.last_name} - Email: {self.email}"
    
# class Admin(models.Model):
#     name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     username = models.CharField(max_length=20)
#     email = models.EmailField()
#     def __str__(self):
#         return f"Nombre: {self.name} - Apellido: {self.last_name} - Username:{self.username} - Email: {self.email} - Staff: {self.is_staff}"


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