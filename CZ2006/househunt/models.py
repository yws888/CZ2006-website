from django.db import models

# Create your models here.

class HDBResaleFlat(models.Model):
    FLATTYPES = (
        ('1 ROOM', '1 ROOM'),
         ('2 ROOM', '2 ROOM'),
        ('3 ROOM', '3 ROOM'),
        ('4 ROOM', '4 ROOM'),
        ('5 ROOM', '5 ROOM'),
        ('EXECUTIVE', 'EXECUTIVE'),
        ('MULTI-GENERATION', 'MULTI-GENERATION'),
        )
    TOWNS = (
        ('ANG MO KIO', 'ANG MO KIO'),
        ('BEDOK', 'BEDOK'),
        ('BISHAN', 'BISHAN'),
        ('BUKIT BATOK', 'BUKIT BATOK'),
        ('BUKIT MERAH', 'BUKIT MERAH'),
        ('BUKIT PANJANG', 'BUKIT PANJANG'),
        ('BUKIT TIMAH', 'BUKIT TIMAH'),
        ('CENTRAL AREA', 'CENTRAL AREA'),
        ('CHOA CHU KANG', 'CHOA CHU KANG'),
        ('CLEMENTI', 'CLEMENTI'),
        ('GEYLANG', 'GEYLANG'),
        ('HOUGANG', 'HOUGANG'),
        ('JURONG EAST', 'JURONG EAST'),
        ('JURONG WEST', 'JURONG WEST'),
        ('KALLANG/WHAMPOA', 'KALLANG/WHAMPOA'),
        ('MARINE PARADE', 'MARINE PARADE'),
        ('PASIR RIS', 'PASIR RIS'),
        ('PUNGGOL', 'PUNGGOL'),
        ('QUEENSTOWN', 'QUEENSTOWN'),
        ('SEMBAWANG', 'SEMBAWANG'),
        ('SENGKANG', 'SENGKANG'),
        ('SERANGOON', 'SERANGOON'),
        ('TAMPINES', 'TAMPINES'),
        ('TOA PAYOH', 'TOA PAYOH'),
        ('WOODLANDS', 'WOODLANDS'),
        ('YISHUN', 'YISHUN'),
    )

    MODELS = (('2-room', '2-room'),
              ('Adjoined flat', 'Adjoined flat'),
              ('Apartment', 'Apartment'),
              ('DBSS', 'DBSS'),
              ('Improved', 'Improved'),
              ('Improved-Maisonette', 'Improved-Maisonette'),
              ('Maisonette', 'Maisonette'),
              ('Model A', 'Model A'),
              ('Model A-Maisonette', 'Model A-Maisonette'),
              ('Model A2', 'Model A2'),
              ('Multi Generation', 'Multi Generation'),
              ('New Generation', 'New Generation'),
              ('Premium Apartment', 'Premium Apartment'),
              ('Premium Apartment Loft', 'Premium Apartment Loft'),
              ('Premium Maisonette', 'Premium Maisonette'),
              ('Simplified', 'Simplified'),
              ('Standard', 'Standard'),
              ('Terrace', 'Terrace'),
              ('Type S1', 'Type S1'),
              ('Type S2', 'Type S2'),
              )

    monthOfSale = models.CharField(max_length=10)
    town = models.CharField(max_length=150, choices = TOWNS, blank = True)
    flatType = models.CharField(max_length=50, choices = FLATTYPES, blank = True)
    blockNo = models.CharField(max_length=10)
    streetName = models.CharField(max_length=150)
    storeyRange = models.CharField(max_length=10, blank = True)
    floorArea = models.FloatField(blank = True)
    flatModel = models.CharField(max_length=50, choices = MODELS, blank = True)
    leaseCommencementYear = models.IntegerField() #TimeField?
    remainingLease = models.IntegerField(blank = True) #calculated by subtracting leaseCommencementYear from 2021
    resalePrice = models.FloatField(blank = True)

    def getTown(self):
        return self.town

    def getStreetName(self):
        return self.streetName

    def __str__(self):
         return self.streetName