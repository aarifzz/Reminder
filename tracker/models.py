from django.db import models

class ProblemRevision(models.Model):
    problem = models.CharField(max_length=255)
    date = models.DateField()

    day_1 = models.BooleanField(default=False)
    day_3 = models.BooleanField(default=False)
    day_5 = models.BooleanField(default=False)
    day_7 = models.BooleanField(default=False)

    def __str__(self):
        return self.problem
