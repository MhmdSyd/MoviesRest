from django.shortcuts import render
from django.http import JsonResponse
from .models import MoviesRest

# Create your views here.

#1 without REST and no model.
def no_rest_no_model(request):
    movies = [{
        'show_id':2344,
        'title': 'Titanic',
        'year':2005

    },
    {
        'show_id':43222,
        'title': 'Avater',
        'year':2012 
    }
    ]


    return JsonResponse(movies, safe=False)



from django.forms.models import model_to_dict
#2.1 model data default djanog without rest
def no_rest_from_model(request):
    data = MoviesRest.objects.all()
    response = list(data.values('show_id', 'title', 'rating'))

    return JsonResponse(response,safe=False)

def no_rest_from_model_filter(request):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    data['params'] = request.GET
    if data['params']:
        show = MoviesRest.objects.filter(show_id=int(data['params'].get('id', ''))).distinct().first()
        obj = MoviesRest.objects.get(id=show.id)
        data['status'] = 'ok'
    else:
        print('none')
        data['status'] = 'bad'
    data['data'] = model_to_dict(obj)

    return JsonResponse(data)


# List == GET
# Create == POST
# pk query == GET 
# Update == PUT
# Delete destroy == DELETE

from rest_framework.decorators import api_view
from .serializer import MoviesSerializers
from rest_framework.response import Response
from rest_framework import status

#3 Function based views 
#3.1 GET POST
@api_view(['GET', 'POST'])
def FBV_list(request):
    if request.method=='GET':
        params = request.GET
        movies = MoviesRest.objects.filter(rating__gte=params.get('rating', ''), year=params.get('year', ''))
        serializer = MoviesSerializers(movies, many=True)
        return Response(serializer.data)
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


# CBV Class based views
from rest_framework.views import APIView
from django.http import Http404
#4.1 List and Create == GET and POST
class CBV_List(APIView):
    
    def get(self, request):
        guests = MoviesRest.objects.all()
        serializer = MoviesSerializers(guests, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MoviesSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)


#4.2 GET PUT DELETE cloass based views -- pk 
class  CBV_pk(APIView):

    def get_object(self, pk):
        try:
            return MoviesRest.objects.get(pk=pk)
        except MoviesRest.DoesNotExists:
            raise Http404
    
    def get(self, request, pk):
        guest = self.get_object(pk)
        serializer = MoviesSerializers(guest)
        return Response(serializer.data)
    
    def put(self, request, pk):
        guest = self.get_object(pk)
        serializer = MoviesSerializers(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        guest = self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#5 Mixins 
from rest_framework import generics, mixins, viewsets
#5.1 mixins list
class mixins_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = MoviesRest.objects.all()
    serializer_class = MoviesSerializers

    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)

#5.2 mixins get put delete 
class mixins_pk(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = MoviesRest.objects.all()
    serializer_class = MoviesSerializers
    def get(self, request, pk):
        return self.retrieve(request)
    def put(self, request, pk):
        return self.update(request)
    def delete(self, request, pk):
        return self.destroy(request)

# 6 Generics 
from rest_framework import generics
#6.1 get and post
class generics_list(generics.ListCreateAPIView):
    queryset = MoviesRest.objects.all()
    serializer_class = MoviesSerializers

#6.2 get put and delete 
class generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoviesRest.objects.all()
    serializer_class = MoviesSerializers


from rest_framework import viewsets
#7 viewsets
class viewsets_movie(viewsets.ModelViewSet):
    queryset = MoviesRest.objects.all()
    serializer_class = MoviesSerializers