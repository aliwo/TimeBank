# Generated by Django 3.1.7 on 2021-04-05 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeBank_app', '0006_messageitem_message_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('register', '신청하기'), ('register_complete', '신청완료'), ('wait', '대기중'), ('complete', '완료하기'), ('fail', '중단')], default='wait', max_length=50),
        ),
    ]
