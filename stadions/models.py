from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Stadion(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    size = models.IntegerField(default=0, help_text="Input Stadion's Size(m²)")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text='input price in USA per hour')
    is_approve = models.BooleanField(default=False)
    is_brone = models.BooleanField(default=False)
    manager = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='Manager_Boy')

    def __str__(self):
        return f"stadion_owner: {self.owner}, stadion_name: {self.name}, price_per_hour: {self.price}"


class OrderStadion(models.Model):
    stadion = models.ForeignKey(Stadion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    stripe_session_id = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f"stadion: {self.stadion}, is_paid: {self.is_paid}"
