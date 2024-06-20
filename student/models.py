from django.db import models


# Create your models here.
class Student(models.Model):   # we are inheriting the mode becase it hall all we need
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    gender = models.CharField(max_length = 7)
    email= models.EmailField()
    date_of_birth = models.DateField()
    code = models.PositiveBigIntegerField()
    country = models.CharField(max_length = 28)
    bio= models.TextField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
