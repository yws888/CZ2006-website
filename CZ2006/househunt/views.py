from django.shortcuts import render
from .forms import HDBSearchForm
from .models import HDBResaleFlat
from django.views.generic import ListView
from django_tables2 import SingleTableView
from .tables import HDBResaleFlatTable
from django.template import RequestContext

from django.http import HttpResponse


def home(request):
    context = { #to pass info to template; can accses data within that template
        #'posts': posts, #info assoc w each post
        'title': 'Home'
    }
    return render(request, 'househunt/home.html', context)

def about(request):
    return render(request, 'househunt/about.html', {'title': 'About'}) #add title if u want a title for the page

def visualise(request):
    return render(request, "househunt/visualise.html", {'title': 'Visualisations'})

def visualise_town(request):
    return render(request, "househunt/visualise-town.html", {'title': 'Town time'})

def visualise_flat_type(request):
    return render(request, "househunt/visualise-flat-type.html", {'title': 'Flat type time'})

def visualise_year(request):
    return render(request, "househunt/visualise-year.html", {'title': 'Year time'})

def calculate(request):
    return render(request, "househunt/calculate.html", {'title': 'Calculate'})

def result(request):
    monthlyIncome = request.POST['num1']
    savings = request.POST['num2']
    cpfBalance = request.POST['num3']


    if monthlyIncome.isdigit() and savings.isdigit() and cpfBalance.isdigit():
        a = int(monthlyIncome)
        b = int(savings)
        c = int(cpfBalance)
        res = a*12 + b + c
        valid = True

        return render(request, "househunt/result.html", {"result": res, "valid": valid})
    else:
        res = "Only digits are allowed"
        valid = False
        return render(request, "househunt/result.html", {"result": res, "valid": valid})


def search(request):
    form = HDBSearchForm(request.GET or None)
    # if form.is_valid():
    #      form.save()
    # #     form = HDBSearchForm()
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
        queryset = queryset.filter(resalePrice__lte = resalePriceInput) # list of objects

    if (request.GET.get('town')) is not '':
        townInput = request.GET.get('town')
        queryset = queryset.filter(town = townInput) # list of objects

    if (request.GET.get('floorArea')) is not '':
        floorAreaInput = int(request.GET.get('floorArea'))
        queryset = queryset.filter(floorArea__lte = floorAreaInput) # list of objects

    if (request.GET.get('flatModel')) is not '':
        flatModelInput = request.GET.get('flatModel')
        queryset = queryset.filter(flatModel = flatModelInput) # list of objects

    table = HDBResaleFlatTable(queryset)
    table.paginate(page=request.GET.get("page", 1), per_page=25)
    return render(request,'househunt/search_result.html', {'table': table})

class HDBResaleFlatView(SingleTableView):
     model = HDBResaleFlat
#    resalePrice__lt = 200000
     table_class = HDBResaleFlatTable
#     template_name = 'househunt/search_result.html'
#
#     def get_queryset(self):
#         query = self.request.GET.get('resalePrice')
#         #flatTypeInput = request.POST['flatType']
#         table_data = HDBResaleFlat.objects.filter(flatType = flatTypeInput)
#         #return render(request, self.template_name, {table_data})
#         return table_data



def map(request):
    flat = HDBResaleFlat.objects.get(id=6888)

    context = {
        'town': flat.town,
        'streetName': flat.streetName, }


    return render(request, "househunt/map.html", context)


def estimate(request):
    form = HDBSearchForm(request.GET or None)

    context = {
        'form': form,
        'title': 'Estimate', }
    return render(request, "househunt/estimate.html", context)
