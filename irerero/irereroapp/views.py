from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.db import models
from .models import School, User

# Create your views here.
def register(request):

    return render(request, 'irereroapp/register1.html')



def register_headteacher(request):
     if request.method == 'POST':
        # Get form data
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        idnumber = request.POST.get('idnumber')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        school_id = request.POST.get('school')
        password = request.POST.get('password')
        role = 'Headteacher'  # You can also modify this based on your logic

        if User.objects.filter(email=email).exists():
                return render(request, 'register_headteacher.html', {'error': 'Email already exists', 'schools': School.objects.all()})
            
            # Get the selected school object
        school = School.objects.get(id=school_id)

        # Create a new user object
        user = User(
            firstname=firstname,
            lastname=lastname,
            national_id=idnumber,
            email=email,
            phonenumber=contact,
            school=school,
            role=role,
            password=make_password(password)  # Hash the password before storing
        )
        
        # Save the user to the database
        user.save()
        
        # Redirect to another page (e.g., a success page)
        return redirect('register_schoolinfo')
     schools = School.objects.all()
     return render(request, 'irereroapp/register_headteacher.html',{'schools': schools})

def register_schoolinfo(request):
     if request.method == 'POST':
        school_name = request.POST.get('schoolName')
        province = request.POST.get('province')
        district = request.POST.get('district')
        sector = request.POST.get('sector')
        cell = request.POST.get('cell')
        village = request.POST.get('village')
        
       
        # Validation (optional)
        if not school_name or not province or not district:
            messages.error(request, "Please complete all required fields.")
            return redirect('register_schoolinfo')

        try:
            # Create a new school record
            school = School.objects.create(
                school_name=school_name,
                province=province,
                district=district,
                sector=sector,
                cell=cell,
                village=village,
            )
            messages.success(request, "School registered successfully!")
            return redirect('register_headteacher')  # Redirect to a success page
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('register_schoolinfo')
        
     return render(request, 'irereroapp/register_schoolinfo.html')

def register_teacher(request):
     if request.method == 'POST':
        # Get form data
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        idnumber = request.POST.get('idnumber')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        school_id = request.POST.get('school')
        password = request.POST.get('password')
        role = 'Teacher'  # You can also modify this based on your logic

        if User.objects.filter(email=email).exists():
                return render(request, 'register_teacher.html', {'error': 'Email already exists', 'schools': School.objects.all()})
            
            # Get the selected school object
        school = School.objects.get(id=school_id)

        # Create a new user object
        user = User(
            firstname=firstname,
            lastname=lastname,
            national_id=idnumber,
            email=email,
            phonenumber=contact,
            school=school,
            role=role,
            password=make_password(password)  # Hash the password before storing
        )
        
        # Save the user to the database
        user.save()
        
        # Redirect to another page (e.g., a success page)
        return redirect('register_schoolinfo')
     schools = School.objects.all()
     return render(request, 'irereroapp/register_teacher.html',{'schools': schools})

def register_parent(request):
     if request.method == 'POST':
        # Get form data
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        idnumber = request.POST.get('idnumber')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        school_id = request.POST.get('school')
        password = request.POST.get('password')
        role = 'Parent'  # You can also modify this based on your logic

        if User.objects.filter(email=email).exists():
                return render(request, 'register_parent.html', {'error': 'Email already exists', 'schools': School.objects.all()})
            
            # Get the selected school object
        school = School.objects.get(id=school_id)

        # Create a new user object
        user = User(
            firstname=firstname,
            lastname=lastname,
            national_id=idnumber,
            email=email,
            phonenumber=contact,
            school=school,
            role=role,
            password=make_password(password)  # Hash the password before storing
        )
        
        # Save the user to the database
        user.save()
        
        # Redirect to another page (e.g., a success page)
        return redirect('register_schoolinfo')
     schools = School.objects.all()
     return render(request, 'irereroapp/register_parent.html',{'schools': schools})

def login(request):
    
    return render(request, 'irereroapp/login.html')