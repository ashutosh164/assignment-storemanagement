from django.contrib import admin
from .models import *


admin.site.register(Inventory)
admin.site.register(InventoryApproval)
admin.site.register(Role)
admin.site.register(UserProfile)
admin.site.register(UserRole)



