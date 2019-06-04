from django.db import models

class Actor(models.Model):
    Name=models.CharField(max_length=50)
    address=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    age=models.PositiveIntegerField()

    def __str__(self):
        return self.Name
