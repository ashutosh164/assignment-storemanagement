from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.role}'

    class Meta:
        unique_together = ('user', 'role',)

    def save(self, *args, **kwargs):
        user = User.objects.get(id=self.user.id)
        if self.role.name == 'Store Manager':
            print(111111111)
            user.is_staff = True
            user.is_superuser = True
            user.save()
        elif self.role.name == 'Department Manager':
            user.is_staff = True
            user.is_superuser = False
            user.save()
        super().save(*args, **kwargs)


class UserProfile(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roles = models.ManyToManyField(Role)


class Inventory(models.Model):
    STATUS_CHOICES = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
    )
    objects = models.Manager()
    product_id = models.CharField(max_length=100, blank=True, null=True)
    product_name = models.CharField(max_length=100)
    vendor = models.CharField(max_length=100)
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    batch_num = models.CharField(max_length=100)
    batch_date = models.DateField(auto_now=True)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')


class InventoryApproval(models.Model):
    objects = models.Manager()
    inventory = models.OneToOneField(Inventory, on_delete=models.CASCADE)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE)
    approved_at = models.DateTimeField(auto_now_add=True)
