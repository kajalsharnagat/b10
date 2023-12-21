from django.shortcuts import render, redirect, HttpResponse
import csv
from .forms import CSVUploadForm
from .models import Employee

def handle_uploaded_csv(csv_file):
    decoded_file = csv_file.read().decode('utf-8').splitlines()
    csv_reader = csv.reader(decoded_file)

    # Assuming your CSV file has headers (first row)
    headers = next(csv_reader) # [headers]
    print(headers)
    for row in csv_reader: # 10
        employee_data = dict(zip(headers, row)) # {"first_name": "aa", "last_name": "bb", "email": "aa@gmail.com"}
        print("employee_data:-  ", employee_data)
        Employee.objects.create(**employee_data)


def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_csv(request.FILES['csv_file'])
            return HttpResponse("File uploaded successfully..!") 
    else:
        form = CSVUploadForm()
    return render(request, 'upload_csv.html', {'form': form})


def download_csv(request):
     # Query the Employee model to get all records
    employees = Employee.objects.all()

    # Create the HttpResponse object with CSV content
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employee_data.csv"'

    # Create the CSV writer and write the header
    csv_writer = csv.writer(response)
    csv_writer.writerow(['first_name', 'last_name', 'email'])  # CSV header

    # Write data rows
    for employee in employees:
        csv_writer.writerow([employee.first_name, employee.last_name, employee.email])

    return response


import csv
from .models import Employee

csv_file_path = 'D:\\Python-B10\\Django_Projects\\LibraryProject\\media\\uploads\\employee.csv'

with open(csv_file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write header
    csv_writer.writerow(['first_name', 'last_name', 'email'])

    # Write data
    employees = Employee.objects.all()
    for employee in employees:
        csv_writer.writerow([employee.first_name, employee.last_name, employee.email])
