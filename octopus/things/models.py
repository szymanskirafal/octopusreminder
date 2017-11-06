from django.core.urlresolvers import reverse
from django.db import models

from ..users.models import User

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True

class Thing(TimeStampedModel):
    text = models.CharField(max_length = 200)
    created_by = models.ForeignKey(User)

    def __str__(self):
        return self.text

    def get_absolut_url(self):
        return reverse('things:detail', args=[str(self.id)])

    class Meta:
        ordering = ['created']
