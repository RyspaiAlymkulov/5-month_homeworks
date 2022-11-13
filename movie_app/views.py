from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieSerializer, ReviewSerializer
from .models import Movie, Review, Director
from rest_framework import status


@api_view(['GET'])
def director_view(request):
    director = Director.objects.all()
    serializer = ReviewSerializer(director, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def director_detail_view(request, id):
    director = Director.objects.get(id=id)
    serializer = ReviewSerializer(director)
    return Response(data=serializer.data)


@api_view(['GET'])
def reviews_view(request):
    review = Review.objects.all()
    serializer = ReviewSerializer(review, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_detail_view(request, id):
    review = Review.objects.get(id=id)
    serializer = ReviewSerializer(review)
    return Response(data=serializer.data)


@api_view(['GET'])
def movies_view(request):
    movie = Movie.objects.all()
    serializer = MovieSerializer(movie, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_detail_view(request, id):
    try:
        post = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Post not found'})
    serializer = MovieSerializer(post)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_view(request):
    dict_ = {
        'movie': 'avengers',
        'title': 'avengers',
        'description': 'мстители вышли в 2012 году',
        'director': 'Кевин Файги'
    }
    return Response(data=dict_)
