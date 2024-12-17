from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.db import models
from .models import School, User, Class, Attendance, child, HealthMetricRecord, HealthMetricType
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .forms import ClassForm
from django.utils import timezone
def login_required(function):
    def wrapper(request, *args, **kwargs):
        if 'user_id' not in request.session:
            messages.error(request, "You must be logged in to access this page.")
            return redirect('login')
        return function(request, *args, **kwargs)
    return wrapper

@login_required
def attendance(request):
    if request.method == "POST":
        # Handle form submission
        child_id = request.POST.get('childName')
        status = request.POST.get('status')
        remarks = request.POST.get('remarks')
        attendance_date = request.POST.get('attendanceDate')

        # Ensure the required fields are provided
        if not child_id or not status:
            messages.error(request, "Please fill out all required fields.")
            return redirect('attendance')

        # Convert status to Boolean
        is_present = True if status == 'Present' else False

        try:
            # Fetch the child record
            child1 = child.objects.get(id=child_id)

            # Save attendance to the database
            Attendance.objects.create(
                child=child1,
                date=attendance_date or timezone.now().date(),
                is_present=is_present,
                remarks=remarks
            )

            # Success message
            messages.success(request, "Attendance successfully recorded!")
            return redirect('attendance')  # Reload the page to clear the form
        except child.DoesNotExist:
            messages.error(request, "Invalid child selected.")
            return redirect('attendance')

    attendance_records = Attendance.objects.select_related('child').all()
    children = child.objects.all()
    return render(request, 'irereroapp/attendance.html',{'attendance': attendance_records,'children': children})

@login_required
def add_class(request):
    if request.method == 'POST':
        form = ClassForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('class-list')  # Replace with your desired redirect view
    else:
        form = ClassForm()
    
    return render(request, 'irereroapp/addclass.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Check if the user exists
            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    # Save user ID in session for login
                    request.session['user_id'] = user.userID
                    messages.success(request, f"Welcome back, {user.firstname}!")
                    return redirect('homepage')  # Replace with your dashboard or homepage URL
                else:
                    messages.error(request, "Invalid password.")
            except User.DoesNotExist:
                messages.error(request, "User with this email does not exist.")
    else:
        form = LoginForm()

    return render(request, 'irereroapp/login.html', {'form': form})

def logout_view(request):
    request.session.flush()  # Clear all session data
    messages.success(request, "You have been logged out.")
    return redirect('landing')

def health(request):
    
    if request.method == 'POST':
            # Get form data from the POST request
            child_id = request.POST.get('student_name')
            metric_type_id = request.POST.get('metric_type')
            metric_value = request.POST.get('metric_value')

            # Ensure required fields are provided
            if not child_id or not metric_value or not metric_type_id:
                messages.error(request, "Please fill out all required fields.")
                return redirect('health')

            try:
                # Fetch the child and metric type records
                selected_child = child.objects.get(id=child_id)
                metric_type = HealthMetricType.objects.get(id=metric_type_id)

                # Create and save the health metric record
                HealthMetricRecord.objects.create(
                    child=selected_child,
                    metric_type=metric_type,
                    value=metric_value
                )

                # Success message
                messages.success(request, "Health metric successfully recorded!")
                return redirect('health')  # Redirect to clear the form
            except child.DoesNotExist:
                messages.error(request, "Invalid child selected.")
                return redirect('health')
            except HealthMetricType.DoesNotExist:
                messages.error(request, "Invalid metric type selected.")
                return redirect('health')

        # Fetch all children and health metric types to populate the dropdowns
    children = child.objects.all()
    metric_types = HealthMetricType.objects.all()

        # Render the template with the children and metric types
    return render(request, 'irereroapp/health.html', {'children': children, 'metric_types': metric_types})



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

def landing(request):
    return render(request, 'irereroapp/landingpage.html')
@login_required
def homepage(request):
    return render(request, 'irereroapp/homepage.html')



