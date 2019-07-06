from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Exam, Employee
from .forms import ContactForm, ExamForm, EmployeeForm ,EditForm


def index(request):
	exams = Exam.objects.filter(published=True)
	return render(request, 'myapp/index.html', { 'exams': exams })

    # id = request.GET.get('id')
	# if id:
	# 	exam = Exam.objects.get(pk=id)
	# return render(request, 'myapp/index.html', { 'exams': exams, 'exam': exam })

def testform(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']

			print(name, email)

	form =ContactForm()
	return render(request, 'myapp/form.html', {'form': form})

def exam_detail(request):
	if request.method == 'POST':
		form = ExamForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(reverse('myapp:exam-form'))
	
	else:
		form = ExamForm(request.POST)
		args = {'form': form}
		return render(request, 'myapp/form.html', args)
# ..........................................................
def Employee_form(request):
	if request.method == 'POST':
			form = EmployeeForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect(reverse('myapp:Employee-form'))
		
	else:
		form = EmployeeForm(request.POST)
		args = {'form': form}
		return render(request, 'myapp/form.html', args)

def my_edit(request, id): 
    instance = get_object_or_404(Employee, id)
    form = EditForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect(reverse('myapp:Employee-form'))
    return render(request, 'myapp/form.html', {'form': form}) 

def view_form(request):
	employee = Employee.objects.filter(published=True)
	return render(request, 'myapp/view-form.html', { 'employee': employee })
	