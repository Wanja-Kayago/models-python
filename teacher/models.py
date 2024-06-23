from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=18)
    date_of_birth = models.DateField()
    education_level = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    bank_account_number = models.IntegerField()
    courses_id = models.ForeignKey(Courses, on_delete=)
    office_hours = models.TimeField()
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
