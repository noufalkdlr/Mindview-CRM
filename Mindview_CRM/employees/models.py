from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
aadhaar_validator = RegexValidator(
     r'^\d{12}$',  # Ensures exactly 12 digits
    'Aadhaar number must be exactly 12 digits.'   
)

class EmployeesDetails(models.Model):
    image = models.ImageField(upload_to='employee_image')
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    d_o_b = models.DateField()
    date_of_joining = models.DateField()
    blood_group = models.CharField(max_length=3)
    Aadhaar_no = models.CharField(max_length=12, unique=True,validators=[aadhaar_validator],)
    
