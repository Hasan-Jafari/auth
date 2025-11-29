from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth import get_user_model

from core.validators import validate_password



class UserManager(BaseUserManager):

    def create_user(self, phone_number, password=None):
        if not phone_number:
            raise ValueError('Phone number is required.')

        User = get_user_model()
        user = User(phone_number=phone_number)

        if password:
            validate_password(password)
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password):
        if not password:
            raise ValueError("Superuser must have a password.")

        user = self.create_user(phone_number, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user
