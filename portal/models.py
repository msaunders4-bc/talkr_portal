from django.db import models

# Create your models here.

# Client model
class Client(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

# Employee model
class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    acc_number = models.CharField(max_length=30)
    embg = models.CharField(max_length=20)
    mk_id = models.CharField(max_length=20)
    start_date = models.DateField()
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if not self.employee_id:
            # Get the last employee ID and increment
            last_employee = Employee.objects.order_by('id').last()
            if last_employee:
                last_id = int(last_employee.employee_id.replace('EMP', ''))
                new_id = last_id + 1
            else:
                new_id = 1
            
            self.employee_id = f'EMP{new_id:04d}'  # EMP0001, EMP0002, etc.
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name