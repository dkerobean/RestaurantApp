from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.decorators import api_view 
from .serializers import FoodSerializer
from dashboard.models import Food
from django.http import JsonResponse
from rest_framework import status



@api_view(['GET'])
def getRoutes(request):
    
    routes = [
        'GET /api', 
        'GET /api/foods', 
        'GET /api/add-food', 
        'GET /api/food/{food-id}',
        'PUT /api/food/{food-id}', 
        'DELETE /api/food/{food-id}',
        
        
    ]
    
    
    return Response(routes)


@api_view(['GET'])
def getFoods(request):
    
    foods = Food.objects.all()
    serializer = FoodSerializer(foods, many=True)
    
    return Response(serializer.data)


@api_view(['POST'])
def addFood(request):
    serializer = FoodSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
   
@api_view(['PUT', 'GET', 'DELETE'])
def foodDetails(request, pk):
    
    try: 
        food = Food.objects.get(id=pk)
    except Food.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    
    if request.method == 'GET':
        serializer = FoodSerializer(food, many=False)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = FoodSerializer(food, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    elif request.method == "DELETE":
        food.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    
    