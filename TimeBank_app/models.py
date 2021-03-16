from django.db import models
from django.conf import settings
from TimeBank_account.models import User

# 거래글 등록
class Post(models.Model): 
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    sevice_choice = (('give','주고싶어요'), ('take','받고싶어요'))
    service = models.CharField(max_length=50, choices=sevice_choice)
    location = models.CharField(max_length=140)
#    work_choice = (())
 #   work = models.CharField(max_length=2, choices=work_choice)
    content = models.CharField(max_length=140, help_text="최대 140자 입력 가능")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 객체 목록 가져오기 (작성 순서대로)
    class Meta:
        ordering = ['-created_at']

    @property
    def index(self):
        return self.work_choice[:50]
