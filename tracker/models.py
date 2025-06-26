from django.db import models

class ProblemRevision(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]
    problem = models.CharField(max_length=255)
    date = models.DateField()
    link = models.URLField( default="", blank=True)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES,default="Easy")
    notes = models.TextField(default="", blank=True)
    day_1 = models.BooleanField(default=False)
    day_3 = models.BooleanField(default=False)
    day_5 = models.BooleanField(default=False)
    day_7 = models.BooleanField(default=False)

    def __str__(self):
        return self.problem
