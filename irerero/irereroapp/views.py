from django.shortcuts import render, redirect
from django.contrib import messages
from .models import School

# Create your views here.
def register(request):

    return render(request, 'irereroapp/register1.html')

def register_headteacher(request):
    return render(request, 'irereroapp/register_headteacher.html')

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