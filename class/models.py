from django.db import models

# Create your models here.
class Class(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    class_name = models.CharField(max_length=20)
    class_id = models.IntegerField()
    teacher_id = models.ForeignKey()
    class_description = models.TextField()
    school_year = models.IntegerField()
    capacity = models.PositiveIntegerField()
    room_number = models.PositiveIntegerField()
    class_best_subject = models.CharField(max_length=30)
    def __str__(self):
        return self.class_name
