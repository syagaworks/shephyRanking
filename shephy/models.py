from django.db import models

class Record(models.Model):
    userName = models.CharField(max_length=50)
    finishTime = models.IntegerField()
    reportedDate = models.DateTimeField(auto_now=True)
