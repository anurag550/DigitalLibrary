from django.contrib import admin

# Register your models here.
from management.models import Course, Student, Issue_Book, Book

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Book)
admin.site.register(Issue_Book)