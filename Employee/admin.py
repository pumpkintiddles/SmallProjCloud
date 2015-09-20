from django.contrib import admin

from Employee.models import Employee

"""
class ChoiceInline(admin.TabularInline):#StackedInline):
    model = Employee
    extra = 3

class EmployeeAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    #fieldsets = [
	#(None,		     {'fields': ['question_text']}),
	#('Date information', {'fields': ['pub_date']}),
    #]
    fieldsets = [
	(None,        {'fields': ['question_text']}),
	('Date info', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']"""

admin.site.register(Employee)
