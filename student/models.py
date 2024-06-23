from django.db import models


# Create your models here.
class Student(models.Model):   # we are inheriting the mode becase it hall all we need
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    gender = models.CharField(max_length = 7)
    email= models.EmailField()
    date_of_birth = models.DateField()
    student = models.PositiveBigIntegerField()
    student_id = models.AutoField()
    country = models.CharField(max_length = 28)
    bio= models.TextField()
    enrollment_date = models.DateField()
    class_id = models.ForeignKey()
    student_guardian = models.CharField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
