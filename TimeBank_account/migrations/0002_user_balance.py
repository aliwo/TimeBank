# Generated by Django 3.1.7 on 2021-04-19 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeBank_account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='balance',
            field=models.IntegerField(default=0, max_length=300, verbose_name='잔액'),
        ),
    ]
