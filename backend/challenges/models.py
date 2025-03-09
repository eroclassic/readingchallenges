from django.db import models

class Challenge(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    query = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title