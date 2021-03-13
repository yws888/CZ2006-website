from django import forms
from .models import HDBResaleFlat

class HDBSearchForm(forms.ModelForm):
    class Meta:
        model = HDBResaleFlat
        town = forms.CharField(required=False)

        fields = [
            'flatType',
            'remainingLease',
            'resalePrice',
            'town',
            # 'monthOfSale',
            # 'storeyRange',
            'floorArea',
            'flatModel'
        ]
        labels = {
            "flatType": "Flat Type",
            "floorArea": "Minimum floor area (in sqm)",
            "resalePrice": "Maximum resale Price"
        }
#
# class RawHDBSearchForm(forms.Form):
#     flatType       = forms.CharField(label='Flat Type', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
#     description = forms.CharField(
#         required=False,
#         widget=forms.Textarea(
#             attrs={
#                 "placeholder": "Your description",
#                 "class": "new-class-name two",
#                 "id": "my-id-for-textarea",
#                 "rows": 20,
#                 'cols': 120
#             }
#         )
#     )
#     price       = forms.DecimalField(initial=199.99)