import math

from django.shortcuts import render
from .forms import HDBSearchForm, HDBEstimateForm, CalculateForm, HDBMapDataForm
from .models import HDBResaleFlat
from django.views.generic import ListView, FormView
from django_tables2 import RequestConfig
from django.views import View

from .tables import HDBResaleFlatTable
from .datavis import readData, DataVisualisation, barPriceVsTown, barPriceVsFlatType, pointPriceVsYear
from django.http import HttpResponseRedirect
import sys
sys.path.append("..") # Adds higher directory to python modules path.

from utility.estimateResalePrice import calculatePrice

class GoogleMapView(View):
    def get(self, request, id):
        flat = HDBResaleFlat.objects.get(id=id)

        form = HDBMapDataForm(request.GET or None, initial = {'address': flat.blockNo + " " + flat.getStreetName()})

        context = {
        'form': form, }
        return render(request, "househunt/gmap.html", context)

class HomeView(View):
    """
    Calling Home View
    """
    template_name = "househunt/home.html"
    def get(self, request):
        """
        Display Home View
        @param self:
        @param request: Request object to generate response for Home

        **Context**
        Will call it just before rendering the template
        ''title''
            Title called Home

        **Template**
        @template:'househunt/home.html'

        @return: an HTTPResponse object with the template of Home
        """
        context = {'title': 'Home'}
        return render(request, self.template_name, context)

class AboutView(View):
    """
    Calling About View
    """
    template_name = "househunt/about.html"
    def get(self, request):
        """
        Display About View
        @param self:
        @param request: Request object to generate response for About

        **Context**
        Will call it just before rendering the template
        ''title''
            Title called About

        **Template**
        @template:'househunt/about.html'

        @return: an HTTPResponse object with the template of About
        """
        context = {'title': 'About'}
        return render(request, self.template_name, context)

class Visualise(View):
    """
    Calling Visualise View with 3 options: By town, by flat type, by year of sale
    """
    template_name = "househunt/visualise.html"
    def get(self, request, id=None, *args, **kwargs):
        """
        Display Visualise View
        @param self:
        @param request: Request object to generate response for Visualise
        @param id:
        @param args: pass the variable number of non keyword arguments to the function
        @param kwargs: pass the variable length of keyword arguments to the function

        **Context**
        ''title''
            Title called Visualisations

        **Template**
        @template:'househunt/visualise.html'

        @return: an HTTPResponse object with the template of Visualise
        """
        context = {'title': 'Visualisations'}
        return render(request, self.template_name, context)

class VisualiseTown(View):
    """
    Calling Visualise By Town View
    """
    template_name = "househunt/visualise-town.html"
    def get(self, request, id=None, *args, **kwargs):
        """
        Display Visualise By Town View
        @param self:
        @param request: Request object to generate response for Visualise By Town
        @param id:
        @param args: pass the variable number of non keyword arguments to the function
        @param kwargs: pass the variable length of keyword arguments to the function

        **Context**
        The static image of Price vs Town bar graph

        **Template**
        @template:'househunt/visualise-town.html'

        @return: an HTTPResponse object with the template of Visualise By Town
        """
        context = readData(barPriceVsTown())
        context.dataToGraph()
        return render(request, self.template_name)

class VisualiseFlatType(View):
    """
    Calling Visualise by Flat Type View
    """
    template_name = "househunt/visualise-flat-type.html"
    def get(self, request, id=None, *args, **kwargs):
        """
        Display Visualise By Flat Type View
        @param self:
        @param request: Request object to generate response for Visualise By Flat Type
        @param id:
        @param args: pass the variable number of non keyword arguments to the function
        @param kwargs: pass the variable length of keyword arguments to the function

        **Context**
        The static image of Price vs Flat Type graph

        **Template**
        @template:'househunt/visualise-flat-type.html'

        @return: an HTTPResponse object with the template of Visualise By Flat Type
        """
        context = readData(barPriceVsFlatType())
        context.dataToGraph()
        return render(request, self.template_name)

class VisualiseYear(View):
    """
    Calling Visualise by Year View
    """
    template_name = "househunt/visualise-year.html"
    def get(self, request, id=None, *args, **kwargs):
        """
        Display Visualise By Year View
        @param self:
        @param request: Request object to generate response for Visualise By Year
        @param id:
        @param args: pass the variable number of non keyword arguments to the function
        @param kwargs: pass the variable length of keyword arguments to the function

        **Context**
        The static image of Price vs Year graph

        **Template**
        @template:'househunt/visualise-year.html'

        @return: an HTTPResponse object with the template of Visualise By Year
        """
        context = readData(pointPriceVsYear())
        context.dataToGraph()
        return render(request, self.template_name)

class CalculateView(View):
    """
    Calling Calculate View, related to @model:'forms.CalculateForm'
    """
    template_name = "househunt/calculate.html"
    def get(self, request, id=None, *args, **kwargs):
        """
        Display Calculate View which requires user to input certain personal information for the system to calculate the maximum affordable price
        @param self:
        @param request: Request object to generate response for Calculate
        @param id:
        @param args: pass the variable number of non keyword arguments to the function
        @param kwargs: pass the variable length of keyword arguments to the function

        **Context**
        ''title''
            Title named Calculate
        ''form''
            CalculateForm from @model:'forms.CalculateForm' that requires user to input:
            - monthly income
            - monthly debt
            - interest rate
            - down payment

        **Template**
        @template: 'househunt/calculate.html'

        @return: an HTTPResponse object with the template of Calculate with the CalculateForm
        """
        form = CalculateForm(request.POST or None)

        context = {
        'form': form,
        'title': 'Calculate', }
        return render(request, self.template_name,context )

    def post(self, request, id=None, *args, **kwargs):
        """
        Display the result of the Calculate View depending on user's input
        @param self:
        @param request: Request object to generate response
        @param id:
        @param args: pass the variable number of non keyword arguments to the function
        @param kwargs: pass the variable length of keyword arguments to the function

        **Context**
        ''result''
            Returns the output of the user's inputs in the form
        ''isPositive''
            Check whether the result is positive

        @return: an HTTPResponse object with the template of Calculate and the result of the user's inputs in the CalculateForm
        """
        monthlyIncome = int(request.POST['monthlyIncome'])
        monthlyDebt = int(request.POST['monthlyDebt'])
        interestRate = float(request.POST['interestRate'])/100
        downPayment = int(request.POST['downPayment'])

        # savings = int(request.POST['savings'])
        # cpfBalance = int(request.POST['cpfBalance'])

        res = (((monthlyIncome*0.28)-monthlyDebt)*12)/interestRate * (1-1/(math.pow((1+interestRate), 30))) + downPayment
        # res = float("{:.2f}".format(res))
        res = int(res)
        if res < 0:
            isPositive = False
        else:
            isPositive = True
        return render(request, "househunt/result.html", {"result": res, "isPositive": isPositive})

class SearchView(View):
    """
    Calling SearchView, related to @model:'forms.HDBSearchForm'
    """
    template_name = "househunt/search.html"
    def get(self, request):
        """
        Display Search View which requires user to input information for the system to return searches that matches user's input
        @param self:
        @param request: Request object to generate response

        **Context**
        ''title''
            Title named Search
        ''form''
            HDBSearchForm from @model:'forms.HDBSearchForm' that requires user to input:
            - flat type
            - remaining lease years
            - maximum resale price
            - town
            - minimum floor area (in sqm)
            - flat model

        **Template**
        @template: 'househunt/search.html'

        @return: an HTTPResponse object with the template of Search with the HDBSearchForm
        """
        form = HDBSearchForm(request.GET or None)

        context = {
            'form': form,
            'title': 'Search', }
        return render(request, self.template_name, context )

class SearchWithPriceView(View):
    """
    Calling Search With maximum affordable Price View, related to @model:'forms.HDBSearchForm'
    """
    def get(self, request, price):
        """
        Display Search View which requires user to input information for the system to return searches that matches user's input after finding out his/her maximum affordability
        @param self:
        @param request: Request object to generate response
        @param price: the maximum affordable price from Calculate Maximum Affordability function

        **Context**
        ''title''
            Title named Search
        ''form''
            HDBSearchForm from @model:'forms.HDBSearchForm' with maximum resale price input filled with the maximum affordable price received that requires user to input:
            - flat type
            - remaining lease years
            - town
            - minimum floor area (in sqm)
            - flat model

        **Template**
        @template: 'househunt/search.html'

        @return: an HTTPResponse object with the template of Search with the HDBSearchForm
        """
        form = HDBSearchForm(request.GET or None, initial = {'resalePrice': price})
        context = {
        'form': form,
        'title': 'Search', }
        return render(request, "househunt/search.html", context)

class SearchResultView(View):
    """
    Calling Search Result View, related to @model:'models.HDBResaleFlat' and @model:'forms.HDBSearchForm'
    """
    def get(self, request):
        """
        Display Search Results View based on the users input
        @param self:
        @param request: Request object to generate response for SearchResult

        **Context**
        ''table''
            Returns the output of the user's inputs in the HDBSearchForm and display in table

        **Template**
        'househunt/search_result.html'

        @return: an HTTPResponse object with the table of the search results based on the user's inputs in the HDBSearchForm
        """
        queryset = HDBResaleFlat.objects.all()

        if (request.GET.get('flatType')) is not '':
            flatTypeInput = request.GET.get('flatType')
            queryset = queryset.filter(flatType = flatTypeInput) # list of objects

        if (request.GET.get('remainingLease')) is not '':
            remainingLeaseInput = request.GET.get('remainingLease')
            queryset = queryset.filter(remainingLease__lte = remainingLeaseInput) # list of objects

        if (request.GET.get('resalePrice')) is not '':
            resalePriceInput = int(request.GET.get('resalePrice'))
            queryset = queryset.filter(resalePrice__lte = resalePriceInput) # return flats with resalePrice <= input

        if (request.GET.get('town')) is not '':
            townInput = request.GET.get('town')
            queryset = queryset.filter(town = townInput) # list of objects

        if (request.GET.get('floorArea')) is not '':
            floorAreaInput = int(request.GET.get('floorArea'))
            queryset = queryset.filter(floorArea__gte = floorAreaInput) # return flats with floorArea >= input

        if (request.GET.get('flatModel')) is not '':
            flatModelInput = request.GET.get('flatModel')
            queryset = queryset.filter(flatModel = flatModelInput) # list of objects

        table = HDBResaleFlatTable(queryset)
        table.paginate(page=request.GET.get("page", 1), per_page=25)
        RequestConfig(request).configure(table)
        return render(request,'househunt/search_result.html', {'table': table})

class MapView(View):
    """
    Calling Map view, related to @model: 'models.HDBResaleFlat'
    """
    template_name = "househunt/map.html"

    def get(self, request, id):
        """
        Display Map View of the flat that user selected
        @param self:
        @param request: Request object to generate response for Map View
        @param id: id of the resale flat

        ''flat''
            An instance from @model:'models.HDBResaleFlat'

        **Context**
        ''town''
            An instance from @model:'models.HDBResaleFlat'
        ''streeName''
            An instance from @model:'models.HDBResaleFlat'

        **Template**
        @template: 'househunt/map.html'

        @return: an HTTPResponse object with the image of the map view based on the flat that user has selected
        """
        flat = HDBResaleFlat.objects.get(id=id)

        context = {
            'town': flat.getTown(),
            'streetName': flat.getStreetName(),
            'blockNo': flat.blockNo,
        }
        return render(request, self.template_name, context)

class EstimateView(View):
    """
    Calling Estimate View, related to @model:'forms.HDBEstimateForm' and @model:'utility.estimatedResalePrice.calculatePrice'
    """
    template_name = "househunt/estimate.html"
    def get(self, request, id=None, *args, **kwargs):
        """
        Display Estimate View which requires user to input information for the system to return estimated selling price for a resale flat
        @param self:
        @param request: Request object to generate response for Estimate
        @param id:
        @param args: pass the variable number of non keyword arguments to the function
        @param kwargs: pass the variable length of keyword arguments to the function

        **Context**
        ''title''
            Title named Estimate
        ''form''
            HDBEstimateForm from @model:'forms.HDBEstimateForm' that requires user to input:
            - flat type
            - remaining lease in years
            - town
            - floor area (in sqm)
            - flat model

        **Template**
        @template: 'househunt/estimate.html'

        @return: an HTTPResponse object with the template of Estimate and the result of the user's inputs in the HDBEstimateForm
        """
        form = HDBEstimateForm(request.POST or None)

        context = {
            'form': form,
            'title': 'Estimate',
        }

        return render(request, self.template_name,context )


    def post(self, request):
        """
        Display the result of the Estimate View depending on user's input
        @param self:
        @param request: Request object to generate response

        **Context**
        ''estimatedResalePrice''
            An int value returned using @model:'utility.estimatedResalePrice.calculatePrice'

        **Template**
        @template: 'househunt/estimate.html'

        if result is < 0:
        @return: an HTTPResponse object with the template of Estimate and the error message
        else:
        @return: an HTTPResponse object with the template of Estimate and the result of the user's inputs in the HDBEstimateForm
        """
        form = HDBEstimateForm(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {
                'form': form})
        flatModelInput = request.POST['flatModel']
        townInput = request.POST['town']
        flatTypeInput = request.POST['flatType']
        floorAreaInput = int(request.POST['floorArea'])
        remainingLeaseInput = float(request.POST['remainingLease'])
        #calculatePrice(town, flatmodel, flattype, remainingl, floorarea):
        estimatedResalePrice =int(calculatePrice(townInput, flatModelInput, flatTypeInput, remainingLeaseInput, floorAreaInput))

        if estimatedResalePrice < 0:
            estimatedResalePrice = 'Error. Unable to provide an accurate estimate of the flat’s selling price'
        return render(request, "househunt/estimate_result.html", {"estimatedResalePrice": estimatedResalePrice})
