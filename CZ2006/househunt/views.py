from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28, 2018'
#     }
# ]


def home(request):
    context = { #to pass info to template; can accses data within that template
        #'posts': posts, #info assoc w each post
        'title': 'Home'
    }
    return render(request, 'househunt/home.html', context)

def about(request):
    return render(request, 'househunt/about.html', {'title': 'About'}) #add title if u want a title for the page

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