from django.contrib import admin
from .models import *

admin.site.register(Log, LogAdmin)
admin.site.register(Asset, AssetAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
