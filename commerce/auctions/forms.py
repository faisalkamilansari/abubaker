from django import forms
from django.utils import timezone

##  Create listing form


class CreateListingForm(forms.Form):
    product_name=forms.CharField(required=True,max_length=64)
    product_image=forms.ImageField(required=True)
    product_price=forms.DecimalField(required=True,max_digits=5,decimal_places=2)
    product_date_joined=forms.DateTimeField(initial=timezone.now)
    product_bid_closing_time=forms.DateTimeField(required=True)
    product_description=forms.CharField(required=True,max_length=100)
    




