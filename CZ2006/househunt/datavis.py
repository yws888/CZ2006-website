"""
Data Visualisation Module
"""
import os

import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib
import matplotlib.pyplot as plt
sb.set(rc={'figure.figsize':(12.7,9.27)})
pd.set_option('display.max_column',None)
pd.set_option('display.max_rows',None)

matplotlib.use('agg')

# read data from a csv file
def readData():
    # columns to read from file
    col_list = ['resale_price','town','flat_type','month']
    # fileName = "CZ2006\\utility\\resale-flat-prices"
    fileName = os.path.join(os.getcwd(), "CZ2006", "utility","resale-flat-prices")

    csvData = pd.read_csv(fileName + '.csv', usecols=col_list)

    # convert month to year
    csvData['year']=csvData['month'].str[:4]
    return csvData

# display a bar graph of the flat's resale price against the town
def barPriceVsTown(csvData):
    plot = sb.barplot(x='resale_price', y='town', data = csvData, ci=None)
    fig = plot.get_figure()
    # save plot to PNG for use in HTML
    fig.savefig(os.path.join(os.getcwd(), "CZ2006", "househunt", "static", "town.png" ), bbox_inches = "tight", dpi = 100)
    #fig.savefig("CZ2006\\househunt\\static\\town.png", bbox_inches = "tight", dpi = 100)
    
# display a bar graph of the flat's resale price against the flat type
def barPriceVsFlatType(csvData):
    plot = sb.barplot(x='resale_price', y='flat_type', data=csvData, ci=None, order=["1 ROOM", "2 ROOM", "3 ROOM", "4 ROOM", "5 ROOM", "EXECUTIVE", "MULTI-GENERATION"])
    fig = plot.get_figure()
    # save plot to PNG for use in HTML
    fig.savefig(os.path.join(os.getcwd(), "CZ2006", "househunt", "static", "flat_type.png" ), bbox_inches = "tight", dpi = 100)
    #fig.savefig('CZ2006\\househunt\\static\\flat_type.png', bbox_inches = "tight", dpi = 100)

# display a point plot of the flat's resale price against the year the resale occurred
def pointPriceVsYear(csvData):
    plot = sb.lineplot(x='year', y='resale_price', data=csvData, ci=None)
    fig = plot.get_figure()
    # save plot to PNG for use in HTML
    fig.savefig(os.path.join(os.getcwd(), "CZ2006", "househunt", "static", "year.png" ), bbox_inches = "tight", dpi = 100)
    # fig.savefig('CZ2006\\househunt\\static\\year.png', bbox_inches = "tight", dpi = 100)
