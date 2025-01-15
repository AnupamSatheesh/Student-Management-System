from django.urls import path
from . import views

urlpatterns = [



    path('', views.home_page_function, name="home_page_function"),
    path('log', views.log_function, name="log_function"),

    # Admin Home Page
    # ---------------
    path('adminhome', views.admin_home_function, name="admin_home_function"),
    # Admin Add teacher
    path('admin_add_teacher', views.admin_add_teacher_function, name="admin_add_teacher_function"),
    # Admin View Teacher
    path('admin_view_teacher', views.admin_view_teacher_function, name="admin_view_teacher_function"),
    # Admin Edit Teacher
    path('admin_edit_teacher/<int:f>', views.admin_edit_teacher_function, name="admin_edit_teacher_function"),
    path('admin_editted_teacher/<int:g>', views.editted_teacher_function, name="editted_teacher_function"),
    # Admin Delete Teacher
    path('admin_delete_teacher/<int:h>', views.admin_delete_teacher_function, name="admin_delete_teacher_function"),

    # Teacher Home Page
    # -----------------
    path('teacherhome', views.teacher_home_function, name="teacher_home_function"),
    # Teacher Own Profile Edition
    path('teacher_edit_profile/<int:i>', views.teacher_edit_profile_function, name="teacher_edit_profile_function"),
    path('teacher_edited_profile/<int:j>', views.teacher_edited_profile_function, name="teacher_edited_profile_function"),
    # Teacher View Students
    path('teacher_view_students', views.teacher_view_students_function, name="teacher_view_students_function"),

    # Student Home Page
    # -----------------
    path('student_home', views.student_home_function, name="student_home_function"),
    path('student_edited_profile', views.student_edited_profile_function, name="student_edited_profile_function"),
    # Student view all teachers
    path('student_view_all_teachers', views.student_view_all_teachers_function, name="student_view_all_teachers"),
    path('student_register_form', views.student_registration_na_function, name="student_registration_na_function"),
    path('student_edit_profile/<int:m>', views.student_edit_profile_function, name="student_edit_profile_function"),
    path('student_edited_profile/<int:n>', views.student_edited_profile_function, name="student_edited_profile_function"),


    # Student and Teacher connections
    path('admin_approved_rejected', views.admin_approved_rejected_function, name="admin_approved_rejected_function"),
    # Admin Rejected
    path('admin_rejected/<int:k>', views.admin_rejected_function, name="admin_rejected_function"),
    # Admin Accepted
    path('admin_accepted/<int:l>', views.admin_accepted_function, name="admin_accepted_function"),
    # Admin View Students
    path('view_students', views.admin_view_students_function, name="admin_view_students_function"),


    # Loging Out
    # ---------- #
    path('admin_logouts', views.admin_logouts_function, name="admin_logouts_function"),
    path('teacher_logouts', views.teacher_logouts_function, name="teacher_logouts_function"),
    path('student_logouts', views.student_logouts_function, name="student_logouts_function"),

    
]