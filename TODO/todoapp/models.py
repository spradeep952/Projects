from django.db import models

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=190, blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
