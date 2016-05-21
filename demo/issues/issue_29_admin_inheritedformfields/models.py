from django.db import models


class Issue29Base(models.Model):
    modified = models.DateTimeField(auto_now_add=True)


class Issue29(Issue29Base):
    content = models.CharField(max_length=250)
