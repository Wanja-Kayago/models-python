from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_id = models.IntegerField()
    teacher_id = models.ForeignKey()
    course_department = models.CharField(max_length=100)
    course_prerequisites = models.TextField()
    course_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course_head = models.CharField(max_length=30)
    enrollment_limit = models.PositiveIntegerField()
    syllabus = models.TextField()
    class_id = models.ForeignKey()
    
    def __str__(self):
        return self.course_name