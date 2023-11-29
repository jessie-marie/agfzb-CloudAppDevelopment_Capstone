from django.db import models
from django.utils.timezone import now


# Create your models here.
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=50)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description: " + self.description


class CarModel(models.Model):
    SEDAN = 'sedan'
    SUV = 'suv'
    WAGON = 'wagon'
    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'Suv'),
        (WAGON, 'Wagon')
    ]
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=50)
    dealer_id = models.IntegerField()
    car_type = models.CharField(max_length=50, choices=CAR_TYPES)
    year = models.DateField()

    def __str__(self):
        return "Name: " + self.name + "," + \
                "Dealer ID: " + str(self.dealer_id) + "," + \
               "Type: " + self.car_type + "," + \
               "Year: " + str(self.year.year)


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
