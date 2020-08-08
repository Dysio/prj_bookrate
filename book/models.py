from django.contrib.auth.models import User
from django.contrib import messages
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
import uuid
from PIL import Image

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=200, blank=False, null=False)
    author = models.CharField(max_length=200, blank=False, null=False)
    year = models.IntegerField(default=None, blank=True, null=True)
    description = models.TextField(default='Book description.')
    image = models.ImageField(default='book.jpg', upload_to='book_covers')

    def __str__(self):
        return f'{self.title}'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Rate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[MinValueValidator(1),
                                           MaxValueValidator(5)])

    def __str__(self):
        return f'{self.book} user: {self.user}'

    class Meta:
        unique_together = ['book','user']


class RateTest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[MinValueValidator(1),
                                           MaxValueValidator(5)])

    def __str__(self):
        return f'{self.book} user: {self.user}'

    class Meta:
        unique_together = ['book','user']


