from django.db import models
from django.utils.timezone import now
from django.contrib.auth.hashers import make_password, check_password
from datetime import date


class User(models.Model):
    ROLE_CHOICES = [
        ('Headteacher', 'Headteacher'),
        ('Teacher', 'Teacher'),
        ('Parent', 'Parent'),
    ]
    
    # Fields for the Users model
    userID = models.AutoField(primary_key=True)  # Automatically increments
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    phonenumber = models.CharField(max_length=15, blank=True, null=True)  # Optional field
    email = models.EmailField(unique=True, blank=True, null=True)  # Ensures unique email
    password = models.CharField(max_length=255, null=False, blank=False)  # Store password hash, not plaintext
    national_id = models.CharField(max_length=20, unique=True)  # Unique National ID
    school = models.ForeignKey('School', on_delete=models.CASCADE,null=True, related_name="users")  

    # You can add additional fields as needed
    status = models.CharField(max_length=20, default='Pending')  # Default status
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set on update

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

# Add a method to verify passwords
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.role})"




class TeacherDetails(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)  # Links to the User table
    school = models.ForeignKey('School', on_delete=models.CASCADE)  # Links to the School table using ForeignKey
    province = models.CharField(max_length=100)  # Province field
    district = models.CharField(max_length=100)  # District field
    sector = models.CharField(max_length=100)  # Sector field
    cell = models.CharField(max_length=100)  # Cell field
    village = models.CharField(max_length=100)  # Village field

    # Optional: Add more fields as needed
    date_added = models.DateTimeField(auto_now_add=True)  # Automatically set when teacher details are added

    def __str__(self):
        return f"Teacher details for {self.user.firstname} {self.user.lastname} at {self.school.school_name}"




class ParentsDetails(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)  # Links to the User table for Parent
    child_name = models.CharField(max_length=255)  # Child's name
    child_dob = models.DateField()  # Child's date of birth
    school = models.ForeignKey('School', on_delete=models.CASCADE)  # Links to the School table using ForeignKey
    
    # Optional: Add more fields if needed, like a reference to the child's class or grade
    date_added = models.DateTimeField(auto_now_add=True)  # Automatically set when parent details are added

    def __str__(self):
        return f"Parent details for {self.user.firstname} {self.user.lastname} with child {self.child_name}"



class School(models.Model):
    school_name = models.CharField(max_length=255)  # The name of the school
    province = models.CharField(max_length=100)  # Province field
    district = models.CharField(max_length=100)  # District field
    sector = models.CharField(max_length=100)  # Sector field
    cell = models.CharField(max_length=100)  # Cell field
    village = models.CharField(max_length=100)  # Village field
    
    date_added = models.DateTimeField(auto_now_add=True)  # Automatically set when the school is added

    def __str__(self):
        return self.school_name



class Class(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    teacher = models.ManyToManyField(User, limit_choices_to={'role': 'Teacher'}, related_name='classes')
    profile_picture = models.ImageField(upload_to='media/', default='SEEL.jpg')
    
    def __str__(self):
        teacher = ", ".join([User.firstname for User in self.teacher.all()])
        return f"{self.name} - Teachers: {teacher}"



class child(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    Dob = models.DateField()  # Store the child's date of birth
    profile_picture = models.ImageField(upload_to='media/', default='default.jpg')
    guardian = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'Parent'}, related_name='children')
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students')
    age = models.PositiveIntegerField()
    
    

    def age(self):
        today = date.today()
        return today.year - self.Dob.year - ((today.month, today.day) < (self.Dob.month, self.Dob.day))

    def __str__(self):
        return self.name


# 5. HealthMetricType Model
class HealthMetricType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)  # e.g., Height, Weight
    unit = models.CharField(max_length=50)  # e.g., cm, kg

    def __str__(self):
        return self.name


# 6. HealthMetric Model
class HealthMetricRecord(models.Model):
    id = models.AutoField(primary_key=True)
    child = models.ForeignKey(child, on_delete=models.CASCADE, related_name='health_metrics')
    metric_type = models.ForeignKey(HealthMetricType, on_delete=models.CASCADE, related_name='metrics')
    value = models.FloatField()
    date_recorded = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.metric_type.name}: {self.value} ({self.child.name})"
    

class Attendance(models.Model):
    child = models.ForeignKey(child, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField(default=now, verbose_name='Attendance Date')
    is_present = models.BooleanField(default=True)
    remarks = models.TextField(blank=True, null=True, verbose_name='Remarks')  # Optional comments about attendance

    class Meta:
        verbose_name = 'Attendance Record'
        verbose_name_plural = 'Attendance Records'
        unique_together = ('child', 'date')  # Ensure one record per student per date
        ordering = ['-date']  # Sort by most recent date

    def __str__(self):
        return f"{self.child.name} - {self.date} - {'Present' if self.is_present else 'Absent'}"

class AttendanceSummary(models.Model):
    child = models.OneToOneField(child, on_delete=models.CASCADE, related_name='attendance_summary')
    total_present = models.PositiveIntegerField(default=0, verbose_name='Total Days Present')
    total_absent = models.PositiveIntegerField(default=0, verbose_name='Total Days Absent')

    def __str__(self):
        return f"{self.child.name} - Present: {self.total_present}, Absent: {self.total_absent}"

# Create your models here.
