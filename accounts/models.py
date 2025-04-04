from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOISES = (
    ('stadion_owner', 'Stadion_Owner'),
    ('manager_of_stadion', "Manager_Of_Stadion"),
    ('simple_user', 'Simple_User')
)


class CustomUser(AbstractUser):
    email = models.EmailField()
    role = models.CharField(max_length=150, choices=ROLE_CHOISES)

    def __str__(self):
        return f"Username: {self.username}, role:{self.role}"




