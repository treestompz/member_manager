from django.db import models


class Member(models.Model):
    ROLE_CHOICES = (
        ("Regular", "Regular"),
        ("Admin", "Admin"),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="Regular")

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"
