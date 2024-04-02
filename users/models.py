from django.db import models

class User(models.Model):
    fullname = models.CharField("Name", max_length=240)
    email = models.EmailField()
    password = models.CharField("Password", max_length=20)
    role = models.CharField("Role", max_length=20, default="user")
    refreshToken = models.CharField("RefreshToken", max_length=40, null=True)
    createdDate = models.DateField("CreatedDate", auto_now_add=True)

    def __str__(self):
        return self.name