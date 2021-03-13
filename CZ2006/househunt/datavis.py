"""
Data Visualisation Module
"""

import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib
import matplotlib.pyplot as plt
sb.set(rc={'figure.figsize':(11.7,8.27)})
# use SVG: Vector graphics format instead of being limited to pixels when saving
matplotlib.use('SVG')
pd.set_option('display.max_column',None)
pd.set_option('display.max_rows',None)


'''def matplotlib_graph(request):
    # Data for plotting
    plt.plot(range(10))
    fig = plt.gcf()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    #image_png = buffer.getvalue()
    #buffer.close()

    string = base64.b64encode(buffer.read())
    graph = urllib.parse.quote(string)

    return render(request, 'visualisations.html', {'graph': graph})'''

# read data from a csv file
def readData():
    # columns to read from file
    col_list = ['resale_price','town','flat_type','month']
    #fileName = input("Enter the csv file name: ")
    fileName = "CZ2006\\utility\\resale-flat-prices"
    csvData = pd.read_csv(fileName + '.csv', usecols=col_list)

    # convert month to year
    csvData['year']=csvData['month'].str[:4]
    return csvData

# display a bar graph of the flat's resale price against the town
def barPriceVsTown(csvData):
    plot = sb.barplot(x='resale_price', y='town', data = csvData)
    fig = plot.get_figure()
    # save plot to PNG for use in HTML
    #graph = plt.fig_to_html(fig)
    fig.savefig("CZ2006\\househunt\\static\\town.png")
    #context = {'graph': graph}
    #return render(request, 'myhtml.html', context)
    
# display a bar graph of the flat's resale price against the flat type
def barPriceVsFlatType(csvData):
    plot = sb.barplot(x='resale_price', y='flat_type', data=csvData, order=["1 ROOM", "2 ROOM", "3 ROOM", "4 ROOM", "5 ROOM", "EXECUTIVE", "MULTI-GENERATION"])
    fig = plot.get_figure()
    # save plot to PNG for use in HTML
    fig.savefig('CZ2006\\househunt\\static\\flat_type.png')

# display a point plot of the flat's resale price against the year the resale occurred
def pointPriceVsYear(csvData):
    plot = sb.lineplot(x='year', y='resale_price', data=csvData)
    fig = plot.get_figure()
    # save plot to PNG for use in HTML
    fig.savefig('CZ2006\\househunt\\static\\year.png')
    

#for debugging
'''def main():
    data = readData()
    barPriceVsTown(data)
    barPriceVsFlatType(data)
    pointPriceVsYear(data)'''
#if __name__ == "__main__":
    #main()
