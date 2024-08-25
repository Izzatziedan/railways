from django.contrib import admin

from .models import Train, Cart, CartTrain, Station, Platform, Route, TimeTable, Journey, JourneyRoute


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ('id', 'serial_number', 'journey_type', 'cart_count')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'serial_number',
        'number_of_seats',
        'level',
        'has_ac',
    )
    list_filter = ('has_ac',)
    raw_id_fields = ('train',)


@admin.register(CartTrain)
class CartTrainAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'train', 'position')
    list_filter = ('cart', 'train')


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city')
    search_fields = ('name',)


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'station')
    list_filter = ('station',)


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_location',
        'second_location',
        'distance',
        'available',
        'comment',
    )
    list_filter = ('first_location', 'second_location', 'available')


@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'departure', 'arrival', 'schedule_type')


@admin.register(Journey)
class JourneyAdmin(admin.ModelAdmin):
    list_display = ('id', 'time_table', 'stop_count')
    list_filter = ('time_table',)
    raw_id_fields = ('route',)


@admin.register(JourneyRoute)
class JourneyRouteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'train',
        'journey',
        'route',
        'departure_time',
        'arrival_time',
        'has_stop_in_arrival',
        'route_order',
        'available_seats',
    )
    list_filter = (
        'train',
        'journey',
        'route',
        'departure_time',
        'arrival_time',
        'has_stop_in_arrival',
    )