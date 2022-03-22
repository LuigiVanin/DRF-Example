from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    birthday = models.DateField()
    
    def __str__(self):
        return self.name
    
    
    
class Major(models.Model): 
    LEVEL = (
        ('B', 'Basic'),
        ('I', 'Itermedium'),
        ('A', 'Advanced')
    )

    major_code = models.CharField(max_length=10)
    about = models.CharField(max_length=100)
    level = models.CharField(max_length=1, choices=LEVEL, blank=False, default='B')
    
    def __str__(self):
        return self.about


class Registration(models.Model):
    class PeriodChoices(models.TextChoices):
        MATUTINO='M'
        VESPERTINO='V'
        NOTURNO='N' 
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    period = models.CharField(choices=PeriodChoices.choices,
                              default=PeriodChoices.MATUTINO,
                              max_length=1,
                              blank=False)
    
    