from django.db import models

# Create your models here.

class Airline(models.Model):
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=100)


    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name



class Seat(models.Model):
    ECONOMY = 'ECO'
    BUSINESS = 'BUI'
    Classes = [
        (ECONOMY, 'Economy'),
        (BUSINESS, 'Business'),
    ]
    # class Classes(models.TextChoices):
    #     ECONOMY = 'ECO', _('Economy')
    #     BUSINESS = 'BUI', _('Business')

    classType = models.CharField(choices=Classes, default=ECONOMY,max_length=3)
    status = models.BooleanField(default=False)
    fare = models.DecimalField(max_digits=6, decimal_places=2)
    flight = models.ForeignKey("Flight", on_delete=models.CASCADE)



    def __str__(self):
        return self.id

class Airplane(models.Model):
    capacity = models.IntegerField()
    airline = models.ForeignKey("Airline", on_delete=models.CASCADE)


class Route(models.Model):
    source = models.ForeignKey("Airport", on_delete=models.CASCADE, related_name='%(class)s_source')
    destination = models.ForeignKey("Airport", on_delete=models.CASCADE, related_name='%(class)s_destination')
    speed = models.IntegerField()
    altitude = models.IntegerField()


class Airport(models.Model):
    name = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name

class Flight(models.Model):
    capacity = models.IntegerField()
    airplane = models.ForeignKey("Airplane", on_delete=models.CASCADE)
    route = models.ForeignKey("Route", on_delete=models.CASCADE)
    departure = models.DateTimeField(auto_now=False, auto_now_add=False)
    arrival = models.DateTimeField(auto_now=False, auto_now_add=False)


    class Meta:
        ordering = ['-departure']

    def __str__(self):
        return self.id
