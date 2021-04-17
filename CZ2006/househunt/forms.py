from django import forms
from .models import HDBResaleFlat, HDBMapData
from django.core import validators
from django_google_maps.widgets import GoogleMapsAddressWidget


class HDBMapDataForm(forms.ModelForm):

    class Meta(object):
        model = HDBMapData
        fields = ['address', 'geolocation']
        labels = {
            "address": "Address (Select the text input bar below and press ENTER to view location on Map)",}
        widgets = {
            "address": GoogleMapsAddressWidget,
        }

class HDBSearchForm(forms.ModelForm):
    """
    Creating HDBEstimateForm from @model:'models.HDBResaleFlat' with the use of inner Meta class
    """

    # remainingLease = forms.IntegerField(label='Remaining Lease in years:',
    #                                     validators=[validators.MaxValueValidator(99), validators.MinValueValidator(44)])
    # floorArea = forms.IntegerField(label='Minimum floor area (in sqm):',
    #                                validators=[validators.MaxValueValidator(249), validators.MinValueValidator(0)])
    # resalePrice = forms.IntegerField(label='Maximum resale Price:',
    #                                validators=[validators.MinValueValidator(0)])


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
    """
    Creating HDBEstimateForm from @model:'models.HDBResaleFlat' with the use of inner Meta class
    """
    def __init__(self, *args, **kwargs):
        """
        Checking whether the fields are filled and ensure that remainingLease is between the value of 0 and 99
        @param args: pass the variable number of non keyword arguments to the function
        @param kwargs: pass the variable length of keyword arguments to the function
        """
        super().__init__(*args, **kwargs)
        self.fields['flatType'].required = True
        #self.fields['remainingLease'].required = True
        self.fields['town'].required = True
        #self.fields['floorArea'].required = True
        self.fields['flatModel'].required = True

    remainingLease = forms.IntegerField(label='Remaining Lease in years:', required = True,
                                        validators=[validators.MaxValueValidator(99), validators.MinValueValidator(44)])
    floorArea = forms.IntegerField(label='Floor area (in sqm):', required = True,
                                        validators=[validators.MaxValueValidator(249), validators.MinValueValidator(0)])
    class Meta:
        model = HDBResaleFlat

        fields = [
            'flatType',
            #'remainingLease',
            'town',
            # 'monthOfSale',
            # 'storeyRange',
            #'floorArea',
            'flatModel'
        ]
        labels = {
            "flatType": "Flat Type",
            #'remainingLease':'Remaining Lease in years',
            #"floorArea": "Floor area (in sqm)",
            "flatModel": "Flat Model",
        }



class CalculateForm(forms.Form):
    """
    Creating CalculateForm
    """
    monthlyIncome = forms.IntegerField(label='Enter Monthly Income:')
    monthlyDebt = forms.IntegerField(label='Enter Monthly Debt:')
    interestRate = forms.FloatField(label='Enter Loan Interest Rate % (with decimal point):')
    downPayment = forms.IntegerField(label='Enter cash towards down payment:')


    # savings = forms.IntegerField(label='Enter savings:')
    # cpfBalance = forms.IntegerField(label='Enter CPF Balance:')
