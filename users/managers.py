from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password):
        """
        Creates and saves a user with the given eamil and password
        """
        if not email:
            raise ValueError("Users must have an email address")
        
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self.db)

        return user
    
    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given eamil and password
        """
        user = self.create_user(email, password)
        user.is_admin = True
        user.save(using=self.db)

        return user