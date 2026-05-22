from django.contrib import admin

# Register your models here.
from .models import Deals, Dealer

admin.site.register(Deals)
admin.site.register(Dealer)