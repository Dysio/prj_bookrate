from django.db import models
import uuid
from PIL import Image

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=200, blank=False, null=False)
    author = models.CharField(max_length=200, blank=False, null=False)
    year = models.IntegerField(default=None, blank=True, null=True)
    description = models.TextField()
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