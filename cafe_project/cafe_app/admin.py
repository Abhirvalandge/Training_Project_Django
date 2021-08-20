from django.contrib import admin
from .models import *

# Register your models here.
# class CoffeeAdmin(models.AdminModel):
#     class Meta:
#         models = CoffeeModel
#         list_display = __all__

admin.site.register(CoffeeModel)
admin.site.register(TeaModel)
admin.site.register(SnacksModel)
