from django.db import models


class Thing(models.Model):
    text = models.CharField(max_length = 200)
