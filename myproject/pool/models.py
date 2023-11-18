from django.db import models

class Pool(models.Model):
    name = models.CharField(max_length=63)
    database = models.CharField(max_length=63)
    mode = models.CharField(max_length=63)
    size = models.IntegerField()
    username = models.CharField(max_length=63)
    pgbouncer_pid = models.IntegerField(null=True)

    def __str__(self):
        return self.name