import sys
import os
import django
import csv

os.chdir("../")
sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = 'CZ2006.settings'
django.setup()

from househunt.models import HDBResaleFlat

HDBResaleFlat.objects.all().delete()



with open(os.path.join(os.getcwd(),  "CZ2006 website", "CZ2006", "utility","resale-flat-prices.csv"),  encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Advance past the header

    for row in post2k:
        HDBResaleFlat.objects.create(month = row[0], town = row[1])