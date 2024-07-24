# myapp/models.py
from django.db import models

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    registered_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    payment = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    teacher_id = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    enroll_id = models.AutoField(primary_key=True)
    date_enrolled = models.DateTimeField(auto_now_add=True)
    payment_status = models.BooleanField(default=False)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.title}"

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    registered_date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name
        

class VideoChat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    scheduled_date = models.DateTimeField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    duration = models.IntegerField(help_text="Duration in minutes")
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course.title} chat scheduled for {self.scheduled_date}"
    
class CourseContent(models.Model):
     content_id = models.AutoField(primary_key=True)
     title = models.CharField(max_length=200)
     description = models.TextField()
     pdf_file = models.FileField(upload_to='pdfs/', blank=True, null=True)
     video = models.FileField(upload_to='videos/', blank=True, null=True)
     course = models.ForeignKey('Course', on_delete=models.CASCADE)
     def __str__(self):
         return self.title