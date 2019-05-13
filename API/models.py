from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
import datetime
# Create your models here.


class Car(models.Model):
    """Car database model"""
    registration_number = models.CharField(max_length=20, validators=[MinLengthValidator(5)], unique=True)
    max_passengers = models.PositiveIntegerField()
    production_year = models.PositiveIntegerField(validators=[
        MinValueValidator(1950),
        MaxValueValidator(datetime.datetime.now().year)]) # year validation
    manufacturer = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    #car type (there can be choices, but I think it will be better to accept user input)
    car_type = models.CharField(max_length=100)
    #category
    ECONOMY, BUSINESS, FIRST = "Ekonomiczna", "Biznesowa", "Pierwsza"
    category_choices = [(ECONOMY, "Ekonomiczna"), (BUSINESS, "Biznesowa"), (FIRST, "Pierwsza")]
    category = models.CharField(max_length=100, choices=category_choices)
    #engine type
    PETROL, HYBRID, ELECTRICAL = "Benzyna/Diesel", "Hybrydowy", "Elektryczny"
    engine_type_choices = [(PETROL, "Benzyna/Diesel"), (HYBRID, "Hybrydowy"), (ELECTRICAL, "Elektryczny")]
    engine_type = models.CharField(max_length=100, choices=engine_type_choices, default=PETROL)

    def __str__(self):
        return f"{self.registration_number}: {self.manufacturer} {self.car_model}"
