from django.db import models

#장고 공식문서 참고
class Blog(models.Model): 
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateField()
    body = models.TextField()

class School(models.Model):
    name = models.CharField(max_length=30)
    school = models.CharField(max_length=30)
    student_id = models.IntegerField()
    certificate_studentship = models.FileField()

class Team(models.Model):
    name = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    fav_food = models.CharField(max_length=30)
    hobby = models.CharField(max_length=30)

    
    