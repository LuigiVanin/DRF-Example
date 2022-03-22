from django.contrib import admin
from django.urls import path, include
from school.views import (
    RegistrationViewSet,
    StudentsViewSet,
    MajorViewSet,
    RegistrationListStudent,
    RegistrationListMajor
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename='students')
router.register('major', MajorViewSet, basename='major')
router.register('reg', RegistrationViewSet, basename='registration')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('students/<int:pk>/reg/', RegistrationListStudent.as_view()),
    path('major/<int:pk>/reg/', RegistrationListMajor.as_view())
]
