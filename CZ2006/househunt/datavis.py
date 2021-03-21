"""
Data Visualisation Module
"""
import os
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
sb.set(rc={'figure.figsize':(12.7,9.27)})
pd.set_option('display.max_column',None)
pd.set_option('display.max_rows',None)


# read data from a csv file
def readData():
    # columns to read from file
    col_list = ['resale_price','town','flat_type','month']
    fileName = os.path.join(os.getcwd(), "CZ2006", "utility","resale-flat-prices.csv")
    csvData = pd.read_csv(fileName, usecols=col_list)
    return pd.DataFrame(csvData)

# display a bar graph of the flat's resale price against the town
def barPriceVsTown(csvData):
    save_location = os.path.join(os.getcwd(), "CZ2006", "househunt", "static", "town.png")
    if not os.path.exists(save_location):
        sb.barplot(x='resale_price', y='town', data = csvData, ci=None)
        # save plot to PNG for use in HTML
        plt.savefig(save_location, bbox_inches = "tight", dpi = 100)
        #fig.savefig("CZ2006\\househunt\\static\\town.png", bbox_inches = "tight", dpi = 100)
        plt.close()
    
# display a bar graph of the flat's resale price against the flat type
def barPriceVsFlatType(csvData):
    save_location = os.path.join(os.getcwd(), "CZ2006", "househunt", "static", "flat_type.png")
    if not os.path.exists(save_location):
        home_types = ["1 ROOM", "2 ROOM", "3 ROOM", "4 ROOM", "5 ROOM", "EXECUTIVE", "MULTI-GENERATION"]
        sb.barplot(x='flat_type', y='resale_price', data=csvData, ci=None, order = home_types)
        # save plot to PNG for use in HTML    
        plt.savefig(save_location, bbox_inches = "tight", dpi = 100)
        #fig.savefig('CZ2006\\househunt\\static\\flat_type.png', bbox_inches = "tight", dpi = 100)
        plt.close()

# display a point plot of the flat's resale price against the year the resale occurred
def pointPriceVsYear(csvData):
    save_location = os.path.join(os.getcwd(), "CZ2006", "househunt", "static", "year.png")
    if not os.path.exists(save_location):
        # convert month to year
        csvData['year']=csvData['month'].str[0:4]
        sb.lineplot(x='year', y='resale_price', data=csvData, ci=None)
        # save plot to PNG for use in HTML
        plt.savefig(save_location, bbox_inches = "tight", dpi = 100)
        # fig.savefig('CZ2006\\househunt\\static\\year.png', bbox_inches = "tight", dpi = 100)
        plt.close()
