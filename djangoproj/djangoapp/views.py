from django.shortcuts import render
from .models import Team #models.py의 Blog 테이블를 가져오자

def home(request):
    team = Team.objects.all() #Blog 테이블에 있는 오브젝트 모두를 불러오기.
    return render(request, 'home.html', {'team':team}) #home.html 과 함께 blogs를 보내준다.