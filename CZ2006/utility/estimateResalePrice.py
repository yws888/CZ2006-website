def calculatePrice(town, flatmodel, flattype, remainingl, floorarea):
    if town=="BISHAN":
        xtown = 99280.849356
    elif town == "BEDOK":
        xtown = -11097.628624
    elif town == "BUKIT BATOK":
        xtown = -89006.593000
    elif town == "BUKIT MERAH":
        xtown = 122398.793046
    elif town == "BUKIT PANJANG":
        xtown = -132432.395942
    elif town == "BUKIT TIMAH":
        xtown = 202068.546746
    elif town == "CENTRAL AREA":
        xtown = 125503.193081
    elif town == "CHOA CHU KANG":
        xtown = -183248.110021
    elif town == "CLEMENTI":
        xtown =  42478.145990
    elif town == "GEYLANG":
        xtown = 42178.369581
    elif town == "HOUGANG":
        xtown = -86854.300475
    elif town == "JURONG EAST":
        xtown = -66780.527882
    elif town == "JURONG WEST":
        xtown = -140701.192175
    elif town == "KALLANG/WHAMPOA":
        xtown = 61607.853297
    elif town == "MARINE PARADE":
        xtown = 164778.865337
    elif town == "PASIR RIS":
        xtown = -111327.585987
    elif town == "PUNGGOL":
        xtown = -131369.990688
    elif town == "QUEENSTOWN":
        xtown = 141707.753194
    elif town == "SEMBAWANG":
        xtown = -201099.714806
    elif town == "SENGKANG":
        xtown = -146652.931832
    elif town == "SERANGOON":
        xtown = -7162.885557
    elif town == "TAMPINES":
        xtown = -52185.521762
    elif town == "TOA PAYOH":
        xtown = 57549.396332
    elif town == "WOODLANDS":
        xtown = -176789.377810
    elif town == "YISHUN":
        xtown = -125828.947728
    else:
        xtown = 0
    if flatmodel=="New Generation":
        xmodel = 13609.868964
    elif flatmodel=="Adjoined flat":
        xmodel = 57992.900307
    elif flatmodel=="Apartment":
        xmodel = 18955.513638
    elif flatmodel=="DBSS":
        xmodel = 153078.137172
    elif flatmodel=="Improved":
        xmodel = -2223.630458
    elif flatmodel=="Improved-Maisonette":
        xmodel = 170588.477415
    elif flatmodel=="Model A":
        xmodel = 6.650883
    elif flatmodel=="Model A-Maisonette":
        xmodel = 117165.087397
    elif flatmodel=="Model A2":
        xmodel = -2028.514293
    elif flatmodel=="Multi Generation":
        xmodel = 113204.354194
    elif flatmodel=="Premium Apartment":
        xmodel = 8784.899432
    elif flatmodel=="Premium Apartment Loft":
        xmodel = 159835.142165
    elif flatmodel=="Premium Maisonette":
        xmodel = 64238.485880
    elif flatmodel=="Simplified":
        xmodel = 10036.341686
    elif flatmodel=="Standard":
        xmodel = 7662.284251
    elif flatmodel=="Terrace":
        xmodel = 335716.463350
    elif flatmodel=="Type S1":
        xmodel = 229031.840746
    elif flatmodel=="Type S2":
        xmodel = 274449.223234
    elif flatmodel=="Maisonette":
        xmodel = 48976.287619
    else:
        xmodel = 0

    if flattype == "1 ROOM":
        xflattype = 0
    elif flattype == "2 ROOM":
        xflattype = 1
    elif flattype == "3 ROOM":
        xflattype = 2
    elif flattype == "4 ROOM":
        xflattype = 3
    elif flattype == "5 ROOM":
        xflattype = 4
    elif flattype == "EXECUTIVE":
        xflattype = 5
    elif flattype == "MULTI-GENERATION":
        xflattype = 6
    else:
        xflattype = -1

    res = -307783.988716 + xtown + xmodel + (xflattype*24787.173062) + (remainingl*5359.995190) + (floorarea*3428.700582)
    return res