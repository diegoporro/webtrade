from django import forms
from django.contrib.auth import (authenticate, get_user_model)
import requests
from django.forms import NumberInput
from .models import *

User = get_user_model()

TRX_OP = [
    ('Buy', 'Buy'),
    ('Sell', 'Sell')
]


def my_choices():
    asst = Asset.objects.all()
    choices = []
    for foo in asst:
        choices.append((foo.name, foo.name))
    return choices


def my_assts():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY=f7f6fd1e-07d1-4a4e-875e-8d9d41936291'
    asst = []
    for foo in range(6):
        # t = []
        def get_latest_crypto_price():
            response = requests.get(url)
            response_json = response.json()

            return response_json['data'][foo]
        asst.append((get_latest_crypto_price().get('quote').get('USD').get('price'), str(get_latest_crypto_price().get('quote').get('USD').get('price')) + ' ' +
                     get_latest_crypto_price().get('name')))
        # asst.append((t[1]))

        # asst.append((get_latest_crypto_price().get('quote').get('USD').get('price'), get_latest_crypto_price().get('name')))
    return asst


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Wrong password or inexist user")
            if not user.check_password(password):
                raise forms.ValidationError("Wrong password or inexist user")
            if not user.is_active:
                raise forms.ValidationError("This user is not active")
        return super(UserLoginForm, self).clean()


class AssetTransacction(forms.Form):
    trx = forms.ChoiceField(choices=TRX_OP, widget=forms.Select(attrs={'class': 'form-control'}))
    asst = forms.ChoiceField(choices=my_assts(), widget=forms.Select(attrs={'class': 'form-control'}))
    qty = forms.FloatField(max_value=10000, min_value=0, widget=NumberInput(attrs={'id': 'form_homework', 'step': "0.01", 'class': 'form-control'}))

    def clean(self):
        trx = self.cleaned_data.get("trx")
        asst = self.cleaned_data.get("asst")
        qty = self.cleaned_data.get("qty")

        return super(AssetTransacction, self).clean()
