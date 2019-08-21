from django import forms
from datetime import datetime
from .models import Item,ExtraCost

class CategoryForm(forms.Form):
    name = forms.CharField(label="Category Name",max_length=200)
    profitmargin = forms.DecimalField(label="Profit Margin (in percent)",max_digits=5,decimal_places=2,required=False)

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['ownusage','image','name','serialnumber','extrainformation','boughtprice','boughtdate','category']

class AddCostForm(forms.ModelForm):
    class Meta:
        model=ExtraCost
        fields = ['information','cost']

class SellForm(forms.Form):
    soldprice = forms.DecimalField(label="Sold for: ",max_digits=7,decimal_places=2)
    solddate = forms.DateTimeField(label="Sold date:",initial=datetime.now())

class ItemEditForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
