from django.db import models


class Review(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.IntegerField()  # 1 a 5 estrellas
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
