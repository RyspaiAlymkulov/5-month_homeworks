from rest_framework import serializers
from .models import Movie, Review, Director
from rest_framework.exceptions import ValidationError


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


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    movie_id = serializers.IntegerField()
    stars = serializers.IntegerField(required=False, max_value=10)

    def validate_movie_id(self, movie_id):
        try:
            Review.objects.get(movie_id=movie_id)
        except:
            raise ValidationError("Choose correct id movie")
        return movie_id


class MovieValidateUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=50)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    director_id = serializers.IntegerField()

    def validate_title(self, title):
        if Movie.objects.filter(title=title):
            raise ValidationError("Select unique name for your movie")
        return title

    class Meta:
        fields = '__all__'

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)

    def validated_name(self, name):
        if Director.objects.filter(name=name):
            raise ValidationError("This name is already exists")
        return name
