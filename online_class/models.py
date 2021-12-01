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