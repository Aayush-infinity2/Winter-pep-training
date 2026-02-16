from django.db import models
from django.contrib.auth.hashers import make_password, check_password, identify_hasher
# Create your models here.
class user(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"
    

class FormModel(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
   
    def __str__(self):
        return self.title
    


class LoginModel(models.Model):
    username=models.CharField(max_length=150,unique=True)
    password=models.CharField(max_length=128)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def set_password(self, raw_password:str) -> None:
        """Hash and set the user's raw password."""
        self.password=make_password(raw_password)

    def check_password(self, raw_password:str) -> bool:
        """Check if the provided raw password matches the stored hashed password."""
        return check_password(raw_password,self.password)
    
    def save(self, *args, **kwargs):
        """Ensure the password is hashed before saving the model."""
        try:
            identify_hasher(self.password)
        except ValueError:
            self.password=make_password(self.password)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.username
    
class SignupModel(models.Model):
    """User model populated via the signup form."""
    username=models.CharField(max_length=150,unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=128)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def set_password(self, raw_password:str) -> None:
        """Hash and set the user's raw password."""
        self.password=make_password(raw_password)
    def check_password(self, raw_password:str) -> bool:
        """Check if the provided raw password matches the stored hashed password."""
        return check_password(raw_password,self.password)
    def save(self, *args, **kwargs):
        """Ensure the password is hashed before saving the model."""
        try:
            identify_hasher(self.password)
        except ValueError:
            self.password=make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
    
class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.message}"
