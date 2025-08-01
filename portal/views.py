from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Employee, Client
from .forms import EmployeeForm


# List view
@login_required
def employee_list(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'portal/employee_list.html', context)


# Detail view
@login_required
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    context = {'employee': employee}
    return render(request, 'portal/employee_detail.html', context)


# Create view
@login_required
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portal:employee_list')  
    else:
        form = EmployeeForm()
    
    context = {'form': form}
    return render(request, 'portal/employee_form.html', context)


# Update view
@login_required
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('portal:employee_detail', pk=employee.pk)  
    else:
        form = EmployeeForm(instance=employee)
    
    context = {'form': form, 'employee': employee}
    return render(request, 'portal/employee_form.html', context)


# Delete view
@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    
    if request.method == 'POST':
        employee.delete()
        return redirect('portal:employee_list')  
    
    context = {'employee': employee}
    return render(request, 'portal/employee_confirm_delete.html', context)
