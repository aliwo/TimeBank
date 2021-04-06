# Generated by Django 3.1.7 on 2021-04-05 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TimeBank_app', '0013_auto_20210405_2311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messageitem',
            name='applicant',
        ),
        migrations.AddField(
            model_name='post',
            name='applicants',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applier', to=settings.AUTH_USER_MODEL),
        ),
    ]
