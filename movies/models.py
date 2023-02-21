from django.db import models


class Ratings(models.TextChoices):
    PG = "PG"
    PG13 = "PG-13"
    R = "R"
    NC17 = "NC-17"
    DEFAULT = "G"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, blank=True)
    rating = models.CharField(
        max_length=20, choices=Ratings.choices, default=Ratings.DEFAULT
    )
    synopsis = models.TextField(null=True, blank=True)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movies"
    )

    orders = models.ManyToManyField(
        "users.User", through="movies.MovieOrder", related_name="movie_orders"
    )


class MovieOrder(models.Model):
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="movie_orders"
    )

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_movie_orders"
    )
