from django.db import models
from django.db.models.fields import IntegerField
from django.contrib.auth.models import AbstractUser # 회원관리 프레임워크

# Create your models here.

class 아이디(AbstractUser):
    pass # 기능을 추가하고 싶으면 pass 대신 기능 추가

class Sale(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class Person(models.Model):
    #회원당 아이디는 1개
    회원 = models.OneToOneField(아이디, on_delete=models.CASCADE)

    # abstractuser에 다 있기 때문에 필요가 없음
    #first_name = models.CharField(max_length=30)
    #last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.회원.username
    