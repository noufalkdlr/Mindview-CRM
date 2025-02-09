# from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify

class EmployeesDetails(models.Model):
    image = models.ImageField(upload_to='employee_image')
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    d_o_b = models.DateField()
    date_of_joining = models.DateField()
    blood_group = models.CharField(max_length=3)
    Aadhaar_no = models.CharField(max_length=14, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    def clean(self):
        digits = self.Aadhaar_no.replace("-", "")  

        if not digits.isdigit() or len(digits) != 12:
            raise ValidationError("Aadhaar number must contain exactly 12 digits (without hyphens).")

        self.Aadhaar_no = f"{digits[:4]}-{digits[4:8]}-{digits[8:]}"


    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = slugify(self.name)
        super().save(*args, **kwargs) 

    def __str__(self):
        return self.name
