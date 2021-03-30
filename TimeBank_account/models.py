from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, UserManager

from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
       
        if not email:
            raise ValueError(('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

# 사용자 정보
class User(AbstractUser):
    
    userid = models.CharField(max_length=64, verbose_name='사용자ID')
    email = models.EmailField(max_length=128, verbose_name='E-mail')
    username = models.CharField(max_length=64, verbose_name='이름', unique=True)
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    contact = models.CharField(max_length=150, verbose_name='연락처')
    birth = models.CharField(max_length=150, verbose_name='생년월일')
    user_age = models.CharField(max_length=50, verbose_name='연령대')
    gender = models.CharField(max_length=10, verbose_name='성별')

    registered_dtn = models.DateField(auto_now_add=True, verbose_name='가입일자')
    # media 폴더 내 'images'파일 저장
    image = models.ImageField(upload_to="images/", blank=True)

    object = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    # 문자열 반환(user_id문자열 반환)
    def __str__(self):
        return self.userid

    class Meta:
        db_table = 'TimeBank_user'


# 계좌정보
class Account(models.Model):
    state_list = (
        ('deal','거래진행중'), ('request','요청진행중'),
        ('complete', '거래완료'), ('inquire', '요청보내기')
        )
    state_type = models.CharField(max_length=10, choices=state_list, verbose_name='요청상태')
    # account_no = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # PositiveIntegerField : 0 또는 양수의 값
    time_balance = models.PositiveIntegerField(default=0, verbose_name='시간계좌')
    transfer_balance = models.IntegerField(default=0, verbose_name='시간거래활동')
    bank = models.CharField(max_length=10)
    account_type_list = (
        ('give','주고싶어요'),
        ('take','받고싶어요')
        )
    account_type = models.CharField(max_length=10, choices=account_type_list)