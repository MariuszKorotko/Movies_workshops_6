from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.views import View
from django.shortcuts import render


class MoviesView(APIView):

    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True, context={"request":
                                                                     request})
        return Response(serializer.data)

class MovieView(APIView):

    def get_object(self, pk):
        """ Get movie by primary key
            Return movie if exist, else raise Http404 page not found
        """
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        movie = self.get_object(id)
        serializer = Movie.serializer(movie, context={"request": request})
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        movie = self.get_object(id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id, format=None):
        movie = self.get_object(id)
        serializer = Movie.serializer(movie, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        serializer = Movie.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonsView(View):

    def get(self, request):
        persons = Person.objects.order_by("name")
        context = {
            "persons": persons
        }
        return render(request, "persons.html", context)