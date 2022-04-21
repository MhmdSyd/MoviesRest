from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from .models import MoviesRest
from .serializer import MoviesSerializers
from django.forms.models import model_to_dict

def no_rest_no_model(request):
    movies=[
        {
            'show_id':244,
            'title':'titanic',
        },
        {
            'show_id':345,
            'title':'avater'
        }
    ]

    return JsonResponse(movies, safe=False)

def no_rest_from_model(request):
    data = MoviesRest.objects.all()
    response = list(data.values('show_id', 'title'))
    return JsonResponse(response, safe=False)


from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response 
from rest_framework import status

from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# from .permissions import IsAuthorOrReadOnly

# Function based view
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def FBV_list(request):
    if request.method == 'GET':
        params = request.GET
        movies = MoviesRest.objects.filter(rating__gte=params.get('rating', ''), year=params.get('year', ''))
        serializer = MoviesSerializers(movies, many=True)
        # print(serializer.data[0])
        # shows = {'shows':serializer.data}
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return render(request, 'show_get.html', context=shows)

    elif request.method=='POST':
        serializer = MoviesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)



#3.1 GET PUT DELET
@api_view(['PUT', 'GET', 'DELETE'])
def FBV_pk(request, pk):
    try:
        movie = MoviesRest.objects.get(show_id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer = MoviesSerializers(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer = MoviesSerializers(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method=='DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


