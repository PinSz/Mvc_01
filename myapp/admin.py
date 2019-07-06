from django.contrib import admin
from .models import Exam, Quiz, Choice, Department, Employee
# Register your models here.
admin.site.site_title = 'e-Exam'
admin.site.site_header = 'e-Exam Administration'

class QuizInline(admin.TabularInline):
	model = Quiz
	extra = 5

class ExamAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    fieldsets = (
		(None, {'fields': ('name', 'description')}),
		('Option', {'fields': ('published',), 'classes': ('collapse',)}),
	)
    list_display = ['name', 'description', 'published']
    list_filter = ['published']
    inlines = [QuizInline]

class ChoiceInline(admin.StackedInline):
	model = Choice

class QuizAdmin(admin.ModelAdmin):
	inlines = [ChoiceInline]
# .....................................
class DepartmentAdmin(admin.ModelAdmin):
	list_display = ['DeptCode', 'DeptName']

class EmployeeAdmin(admin.ModelAdmin):
	list_display = ['EmpNo', 'FName','LName','Sex','Salary','DeptCode']


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)