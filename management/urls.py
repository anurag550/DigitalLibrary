from django.urls import path

from management import views

urlpatterns=[

    path("",views.login_fun,name="login"),
    path("adminreg",views.admin_signup,name="admin_signup"),
    path("studentreg",views.student_reg,name="student_reg"),
    path("admin_home",views.admin_home,name="admin_home"),
    path("student_home",views.student_home,name="student_home"),

    path("addbook", views.add_book, name="add_book"),
    path("diplaybook", views.display_book, name="display_book"),
    path("updatebook/<int:id>", views.update_book, name="update_book"),
    path("deletebook/<int:id>", views.delete_book, name="delete_book"),

    path("displaystudent", views.display_stud, name="display_student"),
    path("updatestudent/<int:id>", views.update_stud, name="update_student"),
    path("deletestud/<int:id>", views.delete_student, name="delete_student"),

    path("assignbook", views.assign_books, name="assign_book"),
    path('readsemester', views.readsemester, name='readsemester'),
    path('readassignbook', views.readassignbook, name='readassignbook'),

    path("issuedbook", views.issued_book, name="issued_book"),
    path('issuebookupdate/<int:id>', views.issuebookupdate, name='issuebookupdate'),
    path('issuebookdelete/<int:id>', views.issubookdelete, name='issuebookdelete'),

    path('student_issued_book', views.studentissuedbook, name='student_issued_book'),
    path("logout", views.logout_fun, name='logout'),

    path('stud_profile', views.profile, name='profile'),
    path('editprofile', views.edit_profile, name='edit_profile'),

]