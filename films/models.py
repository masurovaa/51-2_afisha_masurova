from django.db import models

class Film(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    release_year = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name