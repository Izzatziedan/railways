from django.db import models

CITIES = (
    (0, 'DAMASCUS'),
    (1, 'ALEPPO'),
    (2, 'HOMS'),
    (3, 'LATAKIA'),
    (4, 'TARTOUS'),
    (5, 'HAMAH'),
)

class Train(models.Model):
    JOURNEY_CHOICES = (
        (1,'metro'),
        (2,'domestic'),
        (3,'international'),
    )
    serial_number = models.CharField(max_length=100, null=True, blank=True)
    journey_type = models.IntegerField(choices= JOURNEY_CHOICES,default=1)
    cart_count = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.serial_number

class Cart(models.Model):
    LEVEL_CHOICES = (
        (1,'class A'),
        (2,'class B')
    )
    serial_number = models.CharField(max_length=100, null=True, blank=True)
    number_of_seats = models.IntegerField(default=0)
    level = models.IntegerField(choices=LEVEL_CHOICES,default=1)
    has_ac = models.BooleanField(default=False)
    train = models.ManyToManyField(Train,through='CartTrain')
    # def __str__(self) -> str:
    #     return self.serial_number

class CartTrain(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    position = models.IntegerField(default=-1)



class Station(models.Model):
    name = models.CharField(max_length=30)
    city = models.IntegerField(choices=CITIES, default=-1)
    def __str__(self) -> str:
       return dict(CITIES).get(self.city) + ' ' + self.name


class Platform(models.Model):
    number = models.IntegerField(default=0)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.station.name + '(' + str(self.number) + ')'



class Route(models.Model):
    first_location = models.ForeignKey(Platform,related_name='platform1',on_delete=models.CASCADE)
    second_location = models.ForeignKey(Platform,related_name='platform2',on_delete=models.CASCADE)
    distance = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.first_location.__str__() +' - '+ self.second_location.__str__()


class TimeTable(models.Model):
    SCHEDULE_CHOICES = (
        (1,'metro'),
        (2,'domestic'),
        (3,'international')
    )
    departure = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name='dep')
    arrival = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name='arr')
    schedule_type = models.IntegerField(choices=SCHEDULE_CHOICES,default=-1)
    def __str__(self) -> str:
        return self.departure.__str__() +' - '+ self.arrival.__str__()     



class Journey(models.Model):
    time_table = models.ForeignKey(TimeTable, on_delete=models.CASCADE)
    stop_count = models.IntegerField(default=0)
    # the value 0 applies that it is a direct route from source to destination,
    # which means the arrival station isn't counted as a stop.
    route = models.ManyToManyField(Route, through='JourneyRoute')
    def __str__(self) -> str:
        return self.time_table.__str__()


class JourneyRoute(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    journey = models.ForeignKey(Journey, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    has_stop_in_arrival = models.BooleanField(default=False)
    route_order = models.PositiveSmallIntegerField(default=0)
    available_seats =  models.PositiveIntegerField(default=0)







