from django.contrib import admin
from django.contrib.auth import get_user_model
from django.db import models
import json
User = get_user_model()


class Log(models.Model):
    date_time = models.CharField(max_length=30, null=False, blank=False)
    user = models.CharField(max_length=30, null=False, blank=False)
    transacction = models.CharField(max_length=3, null=False, blank=False)
    asset = models.CharField(max_length=15, null=False, blank=False)
    amount = models.FloatField(max_length=10, null=False, blank=False)

    def __str__(self):
        return self.date_time + ' - ' + self.transacction + ' - ' + self.asset + ' - ' + str(self.amount)


class LogAdmin(admin.ModelAdmin):
    list_display = ('date_time', 'user', 'transacction', 'asset', 'amount')


class Asset(models.Model):
    name = models.CharField(max_length=15, null=False, blank=False)
    price = models.FloatField(max_length=15, null=False, blank=False)

    def __str__(self):
        return self.name


class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


class Portfolio(models.Model):
    amount_avaliable = models.FloatField(max_length=5, null=False, blank=False)
    name = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return str(self.amount_avaliable)


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('amount_avaliable', 'name')
