from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from rest_framework.views import APIView
from .serializers import *
from django.http import Http404
from rest_framework import permissions


class TrainView(APIView):
    permission_classes = [permissions.IsAdminOrReadOnly]
    def get(self, request):
        trains = Train.objects.all()
        serializer = TrainSerializer(trains, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = TrainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TrainDetails(APIView):
    permission_classes = [permissions.IsAdminOrReadOnly]
    def get_object(self, pk):
        try:
           return Train.objects.get(pk=pk)
           
        except Train.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        train = self.get_object(pk)
        serializer = TrainSerializer(train)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        train = self.get_object(pk)
        serializer = TrainSerializer(train,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Cart View
class CartView(APIView):
    permission_classes = [permissions.IsAdminOrReadOnly]
    def get(self, request):
        cart = Cart.objects.all()
        serializer = CartSerializer(cart, many=True, )
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CartDetails(APIView):
    permission_classes = [permissions.IsAdminOrReadOnly]
    def get_object(self, pk):
        try:
           return Cart.objects.get(pk=pk)
           
        except Cart.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        cart = self.get_object(pk)
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        cart = self.get_object(pk)
        serializer = CartSerializer(cart, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Journey View
class JourneyView(APIView):
    permission_classes = [permissions.IsAdminOrReadOnly]
    def get(self, request):
        journey = Journey.objects.all()
        serializer = JourneySerializer(journey, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = JourneySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class JourneyDetails(APIView):
    permission_classes = [permissions.IsAdminOrReadOnly]
    def get_object(self, pk):
        try:
           return Journey.objects.get(pk=pk)
           
        except Journey.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        journey = self.get_object(pk)
        
        
        serializer = JourneySerializer(journey)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        journey = self.get_object(pk)
        serializer = JourneySerializer(journey, data= request.data)
        
        for route in request.data.get('route'):
            journey.route.add(route)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        journey = self.get_object(pk)
        journey.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)