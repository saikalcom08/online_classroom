from django.db import models
from django.conf import settings
# Create your models here.


class UserRegistrationModel(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads', blank=True)

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads', blank=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_id')

    def __str__(self):
        return self.name

class Announcement(models.Model):
    oneA = '1A'
    oneB = '2B'
    oneC = '1C'
    twoA = '2A'
    twoB = '2B'
    YEAR_IN_SCHOOL_CHOICES = [
        (oneA, '1A'),
        (oneB, '1B'),
        (oneC, '1C'),
        (twoA, '2A'),
        (twoB, '2B'),
    ]
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    description = models.TextField()
    group_class = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=oneA,
    )

    def is_upperclass(self):
        return self.group_class in {self.oneB, self.oneC}

    def __str__(self):
        return self.title