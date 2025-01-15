from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import AbstractUser
from . models import User, Teacher, Student_not_approved, Student_approved
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
# Create your views here    
# ---------------------- #
def home_page_function(request):
    return render(request, "home_page.html")


def log_function(request):
    if request.method=='POST':
        un=request.POST.get('u_name')
        pw=request.POST.get('u_password')
        x=authenticate(request, username=un, password=pw)

        # Admin login
        if x is not None and x.is_superuser==1:
            login(request, x)
            request.session['admin_id']=x.id
            return redirect(admin_home_function)
        
        # Teacher login
        elif x is not None and x.usertype=='Teacher':
            login(request, x)
            request.session['teacher_id']=x.id
            return redirect(teacher_home_function)
        
        # Student login
        elif x is not None and x.usertype=='Student':
            login(request, x)
            request.session['student_id']=x.id
            return redirect(student_home_function) 
        
        else:
            return HttpResponse("Please enter the correct login data..........")
    else:
        return render(request, "log.html")
    

# Student Home Page
# ----------------- #

def student_home_function(request):
    n1=request.session['student_id']
    data=User.objects.get(id=n1)
    return render(request, "student_home.html", {'value1':data})

def student_edit_profile_function(request, m):
    st=Student_approved.objects.get(fkstud1=m)
    return render(request, "student_edit_profile.html", {'value':st})

@login_required
def student_edited_profile_function(request, n):
    if request.method=='POST':
        na=request.POST['tna']
        em=request.POST['tem']
        ph=request.POST['tph']
        gn=request.POST['tgn']
        dpt=request.POST['tdpt']
        ag=request.POST['tag']
        un=request.POST['tun']
        pwd=request.POST['tpwd']
        # Fetch the Student object
        student = Student_approved.objects.get(id=n)
        user = student.fkstud1  # Assuming `fkstud1` is the related User object
        # Update User details
        user.set_password(pwd)  # Hash and set the new password
        user.username = un
        user.email = em
        user.usertype = "Student"  # Assuming `usertype` is a custom field
        user.save()
        # Optionally update additional Student fields if needed
        student.name = na
        student.email = em
        student.phoneno = ph
        student.gender = gn     
        student.department = dpt
        student.age = ag
        student.username = un
        student.password = pwd
        student.save()
        return redirect(student_home_function)
    else:
        return redirect(student_home_function)
@login_required
def student_view_all_teachers_function(request):
    st=Teacher.objects.all()
    return render(request, "student_view_all_teachers.html", {'value':st})


# Teacher Home Page
#------------------#
# @login_required
def teacher_home_function(request):
    n1=request.session['teacher_id']
    data=User.objects.get(id=n1)
    return render(request, "teacher_home.html", {'value1': data})

def teacher_edit_profile_function(request, i):
    st=Teacher.objects.get(fteacher=i)
    return render(request, "teacher_edit_profile.html", {'value2': st})

@login_required
def teacher_edited_profile_function(request, j):
    if request.method=='POST':
        na=request.POST['tna']
        em=request.POST['tem']
        ph=request.POST['tph']
        gn=request.POST['tgn']
        dpt=request.POST['tdpt']
        ag=request.POST['tag']
        un=request.POST['tun']
        pwd=request.POST['tpwd']
        # Fetch the teacher object
        teacher = Teacher.objects.get(id=j)
        user = teacher.fteacher  # Assuming `fteacher` is the related User object
        # Update User details
        user.set_password(pwd)  # Hash and set the new password
        user.username = un
        user.email = em
        user.usertype = "Teacher"  # Assuming `usertype` is a custom field
        user.save()
        # Optionally update additional teacher fields if needed
        teacher.name = na
        teacher.email = em
        teacher.phoneno = ph
        teacher.gender = gn
        teacher.department = dpt
        teacher.age = ag
        teacher.username = un
        teacher.password = pwd
        teacher.save()
        return redirect(teacher_home_function)
    else:
        return redirect(teacher_home_function)

@login_required
def teacher_view_students_function(request):
    st=Student_approved.objects.all()
    return render(request, "teacher_view_students.html", {'value': st})
        

# Admin Home Page
#-----------------#
@login_required
def admin_home_function(request):
    n=request.session['admin_id']
    data=User.objects.get(id=n)
    return render(request, "admin_home.html", {'value': data.username})

@login_required
def admin_add_teacher_function(request):
    if request.method=='POST':
        na=request.POST['tname']
        em=request.POST['temail']
        ph=request.POST['tphone']
        gn=request.POST['tgender']
        dpt=request.POST['tdepartment']
        ag=request.POST['tage']
        un=request.POST['tusername']
        pwd=request.POST['tpassword']

        fk=User.objects.create(username=un, email=em, password=pwd, usertype="Teacher")
        st=Teacher.objects.create(name=na, email=em, phoneno=ph, gender=gn, 
                                department=dpt, age=ag, username=un, 
                                password=pwd, fteacher=fk)
        st.save()
        return redirect(admin_home_function)
    else:
        return render(request, "admin_add_teacher.html")
    
@login_required      
def admin_view_teacher_function(request):
    obj=Teacher.objects.all()
    return render(request, "admin_view_teacher.html", {'value': obj})
    # print(obj)

@login_required
def admin_edit_teacher_function(request, f):
    obj=Teacher.objects.get(id=f)
    return render(request, "admin_edit_teacher.html", {'value1': obj})

@login_required
def editted_teacher_function(request, g):
    if request.method=='POST':
        na=request.POST['t_name']
        em=request.POST['t_email']
        ph=request.POST['t_phone']
        gn=request.POST['t_gender']
        dpt=request.POST['t_department']
        ag=request.POST['t_age']
        un=request.POST['t_username']
        pwd=request.POST['t_password']
        # Fetch the teacher object
        teacher = Teacher.objects.get(id=g)
        user = teacher.fteacher  # Assuming `fteacher` is the related User object
        # Update User details
        user.set_password(pwd)  # Hash and set the new password
        user.username = un
        user.email = em
        user.usertype = "Teacher"  # Assuming `usertype` is a custom field
        user.save()
        # Optionally update additional teacher fields if needed
        teacher.name = na
        teacher.email = em
        teacher.phoneno = ph
        teacher.gender = gn
        teacher.department = dpt
        teacher.age = ag
        teacher.username = un
        teacher.password = pwd
        teacher.save()
        return redirect(admin_view_teacher_function)
    else:
        # Handle non-POST requests if necessary
        return redirect(admin_view_teacher_function)

def admin_delete_teacher_function(request, h):
    st=User.objects.get(id=h)
    st.delete()
    return redirect(admin_view_teacher_function)

def admin_view_students_function(request):
    st=Student_approved.objects.all()
    return render(request, "admin_view_students.html", {'value': st})


# Student and User Connection:
# ------------------------------- #

# Student registration
def student_registration_na_function(request):
    if request.method=='POST':
        na=request.POST['stname']
        em=request.POST['stemail']
        ph=request.POST['stphoneno']
        gn=request.POST['stgender']
        dpt=request.POST['stdepartment']
        ag=request.POST['stage']
        un=request.POST['stusername']
        pwd=request.POST['stpassword']
        st=Student_not_approved.objects.create(name=na, email=em, phoneno=ph, gender=gn, 
                                            department=dpt, age=ag, username=un, password=pwd)
        st.save()
        return redirect(home_page_function)
    else:
        return render(request, "student_registration_na.html")
    
# Student ==> User interaction
# -----------------------------
def admin_approved_rejected_function(request):
    st=Student_not_approved.objects.all()
    return render(request, "admin_approved_rejected.html", {'value3': st})

# # Admin Rejected students (deleted)
# # ---------------------------------- #
def admin_rejected_function(request, k):
    st=Student_not_approved.objects.get(id=k)
    st.delete()
    return redirect(admin_approved_rejected_function)

# # Admin Accepted Students
# # ---------------------- #
def admin_accepted_function(request, l):
    fk=Student_not_approved.objects.get(id=l)
    na=fk.name
    em=fk.email
    ph=fk.phoneno
    gn=fk.gender
    dpt=fk.department
    ag=fk.age
    un=fk.username
    pwd=fk.password
    uu=User.objects.create_user(username=un, email=em, password=pwd, usertype="Student")
    u=Student_approved.objects.create(name=na, email=em, phoneno=ph, gender=gn, department=dpt, 
                                      age=ag, username=un, password=pwd, fkstud1=uu)
    u.save()
    fkk=Student_not_approved.objects.get(id=l)
    fkk.delete()
    return redirect(admin_approved_rejected_function)





# Loging Out
#------------#
def admin_logouts_function(request):
    logout(request)
    return redirect(home_page_function)

def teacher_logouts_function(request):
    logout(request)
    return redirect(home_page_function)

def student_logouts_function(request):
    logout(request)
    return redirect(home_page_function)