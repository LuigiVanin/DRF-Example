from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from school.models import Major, Student, Registration
from school.serializer import (
    MajorSerializer,
    RegistrationMajorListSerializer, 
    StudentSerializer, 
    RegistrationSerializer, 
    RegistrationStudentListSerializer
)

class StudentsViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os alunos e alunas'''
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    
class MajorViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os cursos'''
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    
class RegistrationViewSet(viewsets.ModelViewSet):
    '''Listando todas as Matrículas'''
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    

class RegistrationListStudent(ListAPIView):
    '''Listando as matrículas de um aluno'''
    serializer_class = RegistrationStudentListSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    
    
class RegistrationListMajor(ListAPIView):
    '''Listando alunos e alunas matriculadas em um curso'''
    serializer_class = RegistrationMajorListSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Registration.objects.filter(major_id=self.kwargs['pk'])
        return queryset
    