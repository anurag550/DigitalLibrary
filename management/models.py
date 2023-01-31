from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    Course_Name=models.CharField(max_length=30)
    def __str__(self):
        return f"{self.Course_Name}"

class Book(models.Model):
    Book_Name=models.CharField(max_length=30)
    Author_Name=models.CharField(max_length=30)
    Course_ID=models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.Book_Name}"

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Stud_Phone=models.BigIntegerField()
    Stud_Semester=models.IntegerField()
    Stud_Course=models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user}'

class Issue_Book(models.Model):
    Student_Name=models.ForeignKey(User, on_delete=models.CASCADE)
    Book_Name=models.ForeignKey(Book, on_delete=models.CASCADE)
    Issued_Date=models.DateField()
    Valid_Till=models.DateField()












