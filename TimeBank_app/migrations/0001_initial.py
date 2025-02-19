# Generated by Django 3.1.7 on 2021-05-17 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TimeBank_account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('main_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TimeBank_app.maincategory')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=140)),
                ('start_time', models.CharField(max_length=140)),
                ('end_time', models.CharField(max_length=140)),
                ('service', models.CharField(choices=[('주고싶어요', '주고싶어요'), ('받고싶어요', '받고싶어요')], max_length=50)),
                ('location', models.CharField(max_length=140)),
                ('mainwork', models.CharField(choices=[('청소 / 심부름', '청소 / 심부름'), ('몸 가꾸기 / 치장하기', '몸 가꾸기 / 치장하기'), ('수선/ 수리', '수선/ 수리'), ('상담', '상담'), ('이동', '이동'), ('먹기', '먹기'), ('교육 / 여가생활', '교육 / 여가생활'), ('정서지지', '정서지지'), ('돌봄', '돌봄'), ('식물 가꾸기', '식물 가꾸기'), ('모임 장소 대여', '모임 장소 대여'), ('의사소통', '의사소통'), ('건강관리', '건강관리'), ('기타', '기타')], max_length=100, null=True)),
                ('subwork', models.CharField(default='', max_length=200, verbose_name='세부 목록')),
                ('content', models.TextField(verbose_name='내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
                ('tok', models.IntegerField(default=1, verbose_name='거래톡')),
                ('status', models.CharField(choices=[('대기', '대기'), ('진행', '진행'), ('완료', '완료'), ('중단', '중단')], default='대기', max_length=50)),
                ('respond', models.CharField(choices=[('요청대기', '요청대기'), ('요청승인', '요청승인'), ('요청거절', '요청거절')], default='요청대기', max_length=50, verbose_name='승인상태')),
                ('applicants', models.CharField(max_length=140, null=True, verbose_name='신청자')),
                ('giver', models.CharField(max_length=140, null=True, verbose_name='주는사람')),
                ('taker', models.CharField(max_length=140, null=True, verbose_name='받는사람')),
                ('account_no_to', models.CharField(max_length=20, verbose_name='받는사람 계좌번호')),
                ('account_no_from', models.CharField(max_length=20, verbose_name='주는사람 계좌번호')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Post', to='TimeBank_account.account')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
