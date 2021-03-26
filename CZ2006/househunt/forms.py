from django import forms
from .models import HDBResaleFlat

class HDBSearchForm(forms.ModelForm):
    class Meta:
        model = HDBResaleFlat

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
            "resalePrice": "Maximum resale Price",
            'remainingLease':'Remaining Lease in years',
            "flatModel": "Flat Model",
        }

class HDBEstimateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['flatType'].required = True
        self.fields['remainingLease'].required = True
        self.fields['town'].required = True
        self.fields['floorArea'].required = True
        self.fields['flatModel'].required = True

    class Meta:
        model = HDBResaleFlat

        fields = [
            'flatType',
            'remainingLease',
            'town',
            # 'monthOfSale',
            # 'storeyRange',
            'floorArea',
            'flatModel'
        ]
        labels = {
            "flatType": "Flat Type",
            'remainingLease':'Remaining Lease in years',
            "floorArea": "Floor area (in sqm)",
            "flatModel": "Flat Model",
        }

class CalculateForm(forms.Form):
    monthlyIncome = forms.IntegerField(label='Enter Monthly Income:')
    monthlyDebt = forms.IntegerField(label='Enter Monthly Debt:')
    interestRate = forms.FloatField(label='Enter Loan Interest Rate % (to 1 d.p.):')
    # savings = forms.IntegerField(label='Enter savings:')
    # cpfBalance = forms.IntegerField(label='Enter CPF Balance:')
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
