import sys
import os
import django
import csv

# os.chdir("../")
# sys.path.append(os.getcwd())
# os.environ['DJANGO_SETTINGS_MODULE'] = 'CZ2006.settings'
# django.setup()

from househunt.models import HDBResaleFlat

HDBResaleFlat.objects.all().delete()

with open(os.path.join(os.getcwd(), "CZ2006", "utility","resale-flat-prices.csv"),  encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Advance past the header

    for row in reader:
        #templcY = int(2021 - int(row[8])) #calculated by subtracting leaseCommencementYear from 2021
        remainingLease = int(row[9][:2])
        HDBResaleFlat.objects.create(monthOfSale = row[0], town = row[1], flatType = row[2], blockNo = row[3], streetName = row[4], storeyRange = row[5], floorArea= row[6], flatModel = row[7], leaseCommencementYear = row[8], remainingLease = remainingLease, resalePrice = row[10] )