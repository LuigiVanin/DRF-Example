from dataclasses import field, fields
from pyexpat import model
from rest_framework.serializers import SerializerMethodField, ModelSerializer, ReadOnlyField
from school.models import Registration, Student, Major

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id',
            'name',
            'rg',
            'cpf',
            'birthday'
        ]

        
class MajorSerializer(ModelSerializer):
    class Meta:
        model = Major
        fields = '__all__'
        

class RegistrationSerializer(ModelSerializer):
    class Meta:
        model = Registration
        exclude = []
        
        
class RegistrationStudentListSerializer(ModelSerializer):
    major = ReadOnlyField(source='major.about')
    period = SerializerMethodField()
    
    def get_period(self, obj):
        return obj.get_period_display()
    
    class Meta:
        model = Registration
        fields = [
            'major',
            'period'
        ]
        
    
class RegistrationMajorListSerializer(ModelSerializer):
    student_name = ReadOnlyField(source='student.name')
    class Meta:
        model = Registration
        fields = ['student_name']