import math

from django.shortcuts import render
from .forms import HDBSearchForm, HDBEstimateForm, CalculateForm
from .models import HDBResaleFlat
from django.views.generic import ListView
from django_tables2 import SingleTableView, RequestConfig
from django.views import View

from .tables import HDBResaleFlatTable
from .datavis import readData, DataVisualisation, barPriceVsTown, barPriceVsFlatType, pointPriceVsYear
from django.template import RequestContext

from django.http import HttpResponseRedirect
import sys
sys.path.append("..") # Adds higher directory to python modules path.

from utility.estimateResalePrice import calculatePrice


class HomeView(View):
    template_name = "househunt/home.html"
    def get(self, request):
        """

        @param request:
        @return:
        """
        context = {'title': 'Home'}
        return render(request, self.template_name, context)

# def home(request):
#
#     context = { #to pass info to template; can accses data within that template
#         'title': 'Home'  #add title if u want a title for the page
#     }
#     return render(request, 'househunt/home.html', context)


class AboutView(View):
    template_name = "househunt/about.html"
    def get(self, request):
        context = {'title': 'About'}
        return render(request, self.template_name, context)

# def about(request):
#     return render(request, 'househunt/about.html', {'title': 'About'})

class Visualise(View):
    template_name = "househunt/visualise.html"
    def get(self, request, id=None, *args, **kwargs):
        context = {'title': 'Visualisations'}
        return render(request, self.template_name, context)

class VisualiseTown(View):
    template_name = "househunt/visualise-town.html"
    def get(self, request, id=None, *args, **kwargs):
        context = readData(barPriceVsTown())
        context.dataToGraph()
        return render(request, self.template_name)

class VisualiseFlatType(View):
    template_name = "househunt/visualise-flat-type.html"
    def get(self, request, id=None, *args, **kwargs):
        context = readData(barPriceVsFlatType())
        context.dataToGraph()
        return render(request, self.template_name)

class VisualiseYear(View):
    template_name = "househunt/visualise-year.html"
    def get(self, request, id=None, *args, **kwargs):
        context = readData(pointPriceVsYear())
        context.dataToGraph()
        return render(request, self.template_name)

class CalculateView(View):
    template_name = "househunt/calculate.html"
    def get(self, request, id=None, *args, **kwargs):
        form = CalculateForm(request.POST or None)

        context = {
        'form': form,
        'title': 'Calculate', }
        return render(request, self.template_name,context )

    # def calculate(self, request):
    #     form = CalculateForm(request.GET or None)
    #     context = {
    #     'form': form,
    #     'title': 'Calculate', }
    #     return render(request, "househunt/calculate.html", context)

    def post(self, request, id=None, *args, **kwargs):
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

# def result(request):
#     monthlyIncome = int(request.GET['monthlyIncome'])
#     monthlyDebt = int(request.GET['monthlyDebt'])
#     interestRate = float(request.GET['interestRate'])/100
#
#     # savings = int(request.POST['savings'])
#     # cpfBalance = int(request.POST['cpfBalance'])
#
#     res = (((monthlyIncome*0.28)-monthlyDebt)*12)/interestRate * (1-1/(math.pow((1+interestRate), 30)))
#     # res = float("{:.2f}".format(res))
#     res = int(res)
#     return render(request, "househunt/result.html", {"result": res})

class SearchView(View):
    template_name = "househunt/search.html"
    def get(self, request):
        form = HDBSearchForm(request.GET or None)

        context = {
            'form': form,
            'title': 'Search', }
        return render(request, self.template_name,context )

class SearchWithPriceView(View):
    def get(self, request, price):
        form = HDBSearchForm(request.GET or None, initial = {'resalePrice': price})
        context = {
        'form': form,
        'title': 'Search', }
        return render(request, "househunt/search.html", context)

# def search(request):
#     form = HDBSearchForm(request.GET or None)
#     context = {
#          'form': form,
#           'title': 'Search', }
#     return render(request, "househunt/search.html", context)

# def searchPrice(request, price):
#     form = HDBSearchForm(request.GET or None, initial = {'resalePrice': price})
#     context = {
#         'form': form,
#         'title': 'Search', }
#     return render(request, "househunt/search.html", context)

class SearchResultView(View):

    def get(self, request):
        """
        Display Search Results
        @param request:
        @return:
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
    template_name = "househunt/map.html"

    def get(self, request, id):
        flat = HDBResaleFlat.objects.get(id=id)

        context = {
            'town': flat.getTown(),
            'streetName': flat.getStreetName(), }
        return render(request, self.template_name, context)

class EstimateView(View):
    template_name = "househunt/estimate.html"
    def get(self, request, id=None, *args, **kwargs):
        form = HDBEstimateForm(request.POST or None)

        context = {
            'form': form,
            'title': 'Estimate',
        }

        return render(request, self.template_name,context )


    def post(self, request):
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

# def estimate(request):
#     form = HDBEstimateForm(request.POST or None)
#
#     context = {
#         'form': form,
#         'title': 'Estimate', }
#     return render(request, "househunt/estimate.html", context)

# def estimate_result(request):
#     flatModelInput = request.POST['flatModel']
#     townInput = request.POST['town']
#     flatTypeInput = request.POST['flatType']
#     floorAreaInput = int(request.POST['floorArea'])
#     remainingLeaseInput = float(request.POST['remainingLease'])
# #calculatePrice(town, flatmodel, flattype, remainingl, floorarea):
#     estimatedResalePrice =int(calculatePrice(townInput, flatModelInput, flatTypeInput, remainingLeaseInput, floorAreaInput))
#
#     return render(request, "househunt/estimate_result.html", {"estimatedResalePrice": estimatedResalePrice})
