"""
Data Visualisation Module
"""
from __future__ import annotations
from abc import ABC, abstractmethod
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

'''
Reads data then visualises the data depending on user choice
'''
class readData():
    # constructor
    def __init__(self, strategy: DataVisualisation):
        self._strategy = strategy

    def strategy(self):
        return self._strategy

    def strategy(self, strategy: DataVisualisation):
        self._strategy = strategy

    # read data from a csv file
    def dataToGraph(self):
        # columns to read from file
        col_list = ['resale_price','town','flat_type','month']
        fileName = os.path.join(os.getcwd(), "CZ2006", "utility","resale-flat-prices.csv")
        csvData = pd.read_csv(fileName, usecols=col_list)
        self._strategy.displayGraph(csvData)

'''
Strategy Pattern
'''
class DataVisualisation(ABC):
    @abstractmethod
    def displayGraph(self, data):
        pass

'''
ConcreteStrategyA
Display a bar graph of the flat's resale price against the town
'''
class barPriceVsTown(DataVisualisation):
    def displayGraph(self, data):    
        save_location = os.path.join(os.getcwd(), "CZ2006", "househunt", "static", "town.png")
        if not os.path.exists(save_location):
            sb.barplot(x='resale_price', y='town', data = data, ci=None)
            plt.xlabel("Resale Price ($)")
            plt.ylabel("Town")
            # save plot to PNG for use in HTML
            plt.savefig(save_location, bbox_inches = "tight", dpi = 100)
            #fig.savefig("CZ2006\\househunt\\static\\town.png", bbox_inches = "tight", dpi = 100)
            plt.close()
    
'''
ConcreteStrategyB
Display a bar graph of the flat's resale price against the flat type
'''
class barPriceVsFlatType(DataVisualisation):
    def displayGraph(self, data):
        save_location = os.path.join(os.getcwd(), "CZ2006", "househunt", "static", "flat_type.png")
        if not os.path.exists(save_location):
            home_types = ["1 ROOM", "2 ROOM", "3 ROOM", "4 ROOM", "5 ROOM", "EXECUTIVE", "MULTI-GENERATION"]
            sb.barplot(x='flat_type', y='resale_price', data=data, ci=None, order = home_types)
            plt.xlabel("Flat type")
            plt.ylabel("Resale Price ($)")
            # save plot to PNG for use in HTML    
            plt.savefig(save_location, bbox_inches = "tight", dpi = 100)
            #fig.savefig('CZ2006\\househunt\\static\\flat_type.png', bbox_inches = "tight", dpi = 100)
            plt.close()

'''
ConcreteStrategyC
Display a point plot of the flat's resale price against the year the resale occurred
'''
class pointPriceVsYear(DataVisualisation):
    def displayGraph(self, data):
        save_location = os.path.join(os.getcwd(), "CZ2006", "househunt", "static", "year.png")
        if not os.path.exists(save_location):
            # convert month to year
            data['year']=data['month'].str[0:4]
            plt.xlabel("Year of sale")
            plt.ylabel("Resale Price ($)")
            sb.lineplot(x='year', y='resale_price', data=data, ci=None)
            # save plot to PNG for use in HTML
            plt.savefig(save_location, bbox_inches = "tight", dpi = 100)
            # fig.savefig('CZ2006\\househunt\\static\\year.png', bbox_inches = "tight", dpi = 100)
            plt.close()
