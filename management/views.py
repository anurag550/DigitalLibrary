from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache, cache_control

from management.models import Student, Course, Issue_Book, Book

@cache_control(no_catch=True, revalidate=True, nostore=True)
@never_cache
def login_fun(request):
    if request.method == 'POST':
        username = request.POST['txtuser']
        password = request.POST['txtpswd']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_superuser:
                auth.login(request, user)
                request.session["Student_name"] = user.username
                return redirect("admin_home")
            elif user is not user.is_superuser:
                auth.login(request, user)
                request.session["Student_name"] = user.username
                return redirect("student_home")
        else:
            return render(request, "login.html", {'data': 'Invalid user name and password'})
    return render(request, "login.html", {'data': ''})

@cache_control(no_catch=True, revalidate=True, nostore=True)
@never_cache
def admin_signup(request):
    if request.method == "POST":
        user_name = request.POST['txtuser']
        user_password = request.POST['txtpswd']
        user_email = request.POST['txtmail']
        if User.objects.filter(Q(username=user_name) | Q(email=user_email)).exists():
            return render(request, "register.html", {'data': 'Username and email is already exists'})
        else:
            user = User.objects.create_superuser(username=user_name, email=user_email, password=user_password)
            user.save()
            return redirect('login')
    return render(request, "admin_signup.html")

@cache_control(no_catch=True, revalidate=True, nostore=True)
@never_cache
def student_reg(request):
    course = Course.objects.all()
    if request.method == "POST":
        username = request.POST['txtname']
        password = request.POST['txtpswd']
        email= request.POST['txtmail']
        Stud_Phone = request.POST['txtphone']
        Stud_Semester = request.POST['txtsem']
        Stud_Course = Course.objects.get(Course_Name=request.POST['ddlcourse'])
        user = User.objects.create_user(username=username, email=email, password=password)
        student = Student.objects.create(user=user, Stud_Phone=Stud_Phone, Stud_Semester=Stud_Semester, Stud_Course=Stud_Course)
        user.save()
        student.save()
        return redirect('login')
    return render(request, "student_signup.html", {'Course_Data': course})


@login_required
@cache_control(no_catch=True, revalidate=True, nostore=True)
@never_cache
def admin_home(request):
    n1 = request.session.get('Student_name')
    return render(request, "admin_home.html", {'data': n1})


@login_required
@cache_control(no_catch=True, revalidate=True, nostore=True)
@never_cache
def student_home(request):
    n1 = request.session.get('Student_name')
    return render(request, "student_home.html",{'data': n1})


@login_required
@cache_control(no_catch=True, revalidate=True, nostore=True)
@never_cache
def add_book(request):
    course = Course.objects.all()
    if request.method == "POST":
        b1 = Book()
        b1.Book_Name = request.POST['txtbook']
        b1.Author_Name = request.POST['txtauthor']
        b1.Course_ID = Course.objects.get(Course_Name=request.POST['ddlcourse'])
        b1.save()
        return redirect("add_book")
    return render(request, "add_books.html", {'Course_Data': course})


@login_required
@cache_control(no_catch=True, revalidate=True, nostore=True)
@never_cache
def display_book(request):
    b1 = Book.objects.all()
    return render(request, "display_books.html", {'data': b1})


@login_required
@cache_control(no_catch=True, revalidate=True, nostore=True)
@never_cache
def update_book(request, id):
    b1 = Book.objects.get(id=id)
    course = Course.objects.all()
    if request.method == 'POST':
        b1.Book_Name = request.POST['txtbook']
        b1.Author_Name = request.POST['txtauthor']
        b1.Course_ID = Course.objects.get(Course_Name=request.POST['ddlcourse'])
        b1.save()
        return redirect('display_book')
    return render(request, 'update_books.html', {'data': b1, 'Course_Data': course})


def delete_book(request, id):
    b1 = Book.objects.get(id=id)
    b1.delete()
    return redirect("display_book")

@login_required
@cache_control(no_catch=True, revalidate=True, nostore=True)
@never_cache
def display_stud(request):
    s1 = Student.objects.all()
    return render(request, "display_students.html", {'data': s1})

@login_required
@cache_control(no_catch=True, revalidate=True, nostore=True)
@never_cache
def update_stud(request, id):
    s1 = Student.objects.get(id=id)
    course = Course.objects.all()
    if request.method == "POST":
        s1.user.username = request.POST["txtname"]
        print(s1.user.username)
        s1.Stud_Phone = request.POST["txtphone"]
        s1.Stud_Semester = request.POST["txtsem"]
        s1.Stud_Course = Course.objects.get(Course_Name=request.POST["ddlcourse"])
        s1.save()
        s1.user.save()
        return redirect('display_student')
    return render(request, "update_students.html", {'data': s1, 'Course_Data': course})


def delete_student(request, id):
    s1 = Student.objects.get(id=id)
    s1.delete()
    return redirect("display_student")

@login_required
@cache_control(no_catch=True, revalidate=True, nostore=True)
@never_cache
def assign_books(request):
    c1 = Course.objects.all()
    return render(request, 'assign_book.html', {'data': c1})

@login_required
@cache_control(no_catch=True, revalidate=True, nostore=True)
@never_cache
def readsemester(request):
    student_semester = request.POST['txtsem']
    student_course = Course.objects.get(Course_Name=request.POST['ddlcourse'])
    student = Student.objects.filter(Q(Stud_Semester=student_semester) & Q(Stud_Course=student_course))
    print(student)
    book = Book.objects.filter(Q(Course_ID=Course.objects.get(Course_Name=student_course)))
    return render(request, 'assign_book.html', {'Students': student, 'Books': book})

@login_required
@cache_control(no_catch=True, revalidate=True, nostore=True)
@never_cache
def readassignbook(request):
    ib = Issue_Book()
    ib.Student_Name = User.objects.get(username=request.POST['ddlSname'])
    ib.Book_Name = Book.objects.get(Book_Name=request.POST['ddlSbook'])
    ib.Issued_Date = request.POST['startDate']
    ib.Valid_Till = request.POST['endDate']
    ib.save()
    return redirect('assign_book')

@login_required
@cache_control(no_catch=True, revalidate=True, nostore=True)
@never_cache
def issued_book(request):
    ib = Issue_Book.objects.all()
    return render(request, "issued_book.html", {'data': ib})

@login_required
@cache_control(no_catch=True, revalidate=True, nostore=True)
@never_cache
def issuebookupdate(request, id):
    ib = Issue_Book.objects.get(id=id)
    if request.method == 'POST':
        ib.Student_Name = Student.objects.get(Stud_Name=request.POST['txtStudentName'])
        ib.Book_Name = Book.objects.get(Book_Name=request.POST['txtBookName'])
        ib.Issued_Date = request.POST['txtissuedDate']
        ib.Valid_Till = request.POST['txtvalidtill']
        ib.save()
        return redirect('issued_book')
    return render(request, 'issuebookupdate.html', {'data': ib})


def issubookdelete(request, id):
    ib = Issue_Book.objects.get(id=id)
    ib.delete()
    return redirect('issued_book')


@login_required
@cache_control(no_catch=True, revalidate=True, nostore=True)
@never_cache
def studentissuedbook(request):
    ib = Issue_Book.objects.filter(Student_Name=User.objects.get(username=request.session['Student_name']))
    return render(request, 'student_issued_book.html', {'data': ib})

def logout_fun(request):
    auth.logout(request)
    return redirect("/")

@login_required
@cache_control(no_catch=True, revalidate=True, nostore=True)
@never_cache
def profile(request):
    n2 = request.session.get('Name')
    return render(request,'stud_profile.html',{'data':n2})

@login_required
@cache_control(no_catch=True, revalidate=True, nostore=True)
@never_cache
def edit_profile(request):
    s1 = Student.objects.get(user=request.user)
    course = Course.objects.all()
    if request.method == "POST":
        s1.user.username = request.POST["txtname"]
        print(s1.user.username)
        s1.Stud_Phone = request.POST["txtphone"]
        s1.Stud_Semester = request.POST["txtsem"]
        s1.Stud_Course = Course.objects.get(Course_Name=request.POST["ddlcourse"])
        s1.save()
        s1.user.save()
        return redirect('profile')
    return render(request, "edit_student_profile.html", {'data': s1, 'Course_Data': course})