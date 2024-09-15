from django.db import models

# Create your models here.


class Book(models.Model):
    """Books reading currently"""
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation fo the model"""
        return self.name


class Summary(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    entry = models.TextField()

    class Meta:
        verbose_name_plural = 'summaries'

    def __str__(self):
        return self.entry[:50] + "..."
