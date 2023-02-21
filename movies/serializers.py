from rest_framework import serializers
from .models import Movie, Ratings, MovieOrder


class MovieSerielizer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null=True, default=None)
    rating = serializers.ChoiceField(choices=Ratings.choices, default=Ratings.DEFAULT)
    synopsis = serializers.CharField(allow_null=True, default=None)

    added_by = serializers.EmailField(source="user.email", read_only=True)

    def __str__(self) -> str:
        return f"<Movie ({self.title}) - {self.id}>"

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(source="movie.title", read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.EmailField(source="user.email", read_only=True)
    buyed_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data: dict) -> MovieOrder:
        return MovieOrder.objects.create(**validated_data)
