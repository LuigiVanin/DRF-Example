from django.contrib import admin
from school.models import Major, Student, Registration

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rg', 'cpf')
    list_display_link = ('id', 'name')
    search_fields = ('name', )
    list_per_page = 20
    

class MajorAdmin(admin.ModelAdmin):
    list_display = ('id', 'major_code', 'about', 'level')
    list_display_link = ('id', 'major_code')
    search_fields = ('major_code', )
    list_per_page = 20
    
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'major', 'period')
    list_display_link = ('id', 'student')
    
admin.site.register(Student, StudentsAdmin)
admin.site.register(Major, MajorAdmin)
admin.site.register(Registration, RegistrationAdmin)

