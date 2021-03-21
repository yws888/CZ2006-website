import math

from django.shortcuts import render
from .forms import HDBSearchForm, HDBEstimateForm, CalculateForm
from .models import HDBResaleFlat
from django.views.generic import ListView
from django_tables2 import SingleTableView, RequestConfig
from django.views import View

from .tables import HDBResaleFlatTable
from .datavis import readData, barPriceVsTown, barPriceVsFlatType, pointPriceVsYear
from django.template import RequestContext

from django.http import HttpResponseRedirect
import sys
sys.path.append("..") # Adds higher directory to python modules path.

from utility.estimateResalePrice import calculatePrice


def home(request):
    context = { #to pass info to template; can accses data within that template
        'title': 'Home'  #add title if u want a title for the page
    }
    return render(request, 'househunt/home.html', context)


class AboutView(View):
    template_name = "househunt/about.html"
    def get(self, request, id=None, *args, **kwargs):
        context = {'title': 'About'}
        return render(request, self.template_name, context)

# def about(request):
#     return render(request, 'househunt/about.html', {'title': 'About'})

def visualise(request):
    return render(request, "househunt/visualise.html", {'title': 'Visualisations'})

def visualise_town(request):
    barPriceVsTown(readData())
    return render(request, "househunt/visualise-town.html", {'title': 'Town time'})

def visualise_flat_type(request):
    barPriceVsFlatType(readData())
    return render(request, "househunt/visualise-flat-type.html", {'title': 'Flat type time'})

def visualise_year(request):
    pointPriceVsYear(readData())
    return render(request, "househunt/visualise-year.html", {'title': 'Year time'})

def calculate(request):
    form = CalculateForm(request.POST or None)
    context = {
    'form': form,
    'title': 'Calculate', }
    return render(request, "househunt/calculate.html", context)

def result(request):
    monthlyIncome = int(request.POST['monthlyIncome'])
    monthlyDebt = int(request.POST['monthlyDebt'])
    interestRate = float(request.POST['interestRate'])

    # savings = int(request.POST['savings'])
    # cpfBalance = int(request.POST['cpfBalance'])

    # res = monthlyIncome*12 + savings + cpfBalance

    res = (((monthlyIncome*0.28)-monthlyDebt)*12)/interestRate * (1-1/(math.pow((1+interestRate), 30)))
    # res = float("{:.2f}".format(res))
    res = int(res)
    return render(request, "househunt/result.html", {"result": res})

def search(request):
    form = HDBSearchForm(request.GET or None)
    # else:
    #     form = HDBSearchForm(request.GET or None)
    # if form.is_valid():
    #      form.save()
    # #     form = HDBSearchForm()
    context = {
         'form': form,
          'title': 'Search', }
    return render(request, "househunt/search.html", context)

def searchPrice(request, price):
    form = HDBSearchForm(request.GET or None, initial = {'resalePrice': price})
    context = {
        'form': form,
        'title': 'Search', }
    return render(request, "househunt/search.html", context)

def search_result(request):
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

class HDBResaleFlatView(SingleTableView):
     model = HDBResaleFlat
     table_class = HDBResaleFlatTable
#     template_name = 'househunt/search_result.html'
#
#     def get_queryset(self):
#         query = self.request.GET.get('resalePrice')
#         #flatTypeInput = request.POST['flatType']
#         table_data = HDBResaleFlat.objects.filter(flatType = flatTypeInput)
#         #return render(request, self.template_name, {table_data})
#         return table_data



def map(request, id):
    flat = HDBResaleFlat.objects.get(id=id)

    context = {
        'town': flat.town,
        'streetName': flat.streetName, }
    return render(request, "househunt/map.html", context)


def estimate(request):
    form = HDBEstimateForm(request.POST or None)

    context = {
        'form': form,
        'title': 'Estimate', }
    return render(request, "househunt/estimate.html", context)

def estimate_result(request):
    flatModelInput = request.POST['flatModel']
    townInput = request.POST['town']
    flatTypeInput = request.POST['flatType']
    floorAreaInput = int(request.POST['floorArea'])
    remainingLeaseInput = float(request.POST['remainingLease'])
#calculatePrice(town, flatmodel, flattype, remainingl, floorarea):
    estimatedResalePrice =int(calculatePrice(townInput, flatModelInput, flatTypeInput, remainingLeaseInput, floorAreaInput))

    return render(request, "househunt/estimate_result.html", {"estimatedResalePrice": estimatedResalePrice})
