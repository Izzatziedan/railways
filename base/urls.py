from django.urls import path
from .views import *
urlpatterns = [
    path('train/', TrainView.as_view()),
    path('train/<int:pk>', TrainDetails.as_view()),
    path('cart/', CartView.as_view()),
    path('cart/<int:pk>', CartDetails.as_view()),
    path('journey/', JourneyView.as_view()),
    path('journey/<int:pk>', JourneyDetails.as_view()),
]