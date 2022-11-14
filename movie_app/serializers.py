from rest_framework import serializers
from .models import Movie, Review, Director


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description duration director stars'.split()


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name movies_count'.split()


class DirectorCountSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'movies_count'.split()

    def get_movie_count(self, movie):
        return movie.all().count()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars movie'.split()


class MovieReviewSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many=True)
    director = DirectorSerializer()

    class Meta:
        model = Movie
        fields = 'id title description duration director review rating'.split()