# Generated by Django 3.1.7 on 2021-04-06 23:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TimeBank_app', '0015_auto_20210406_0133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messageitem',
            name='author',
        ),
        migrations.AddField(
            model_name='post',
            name='respond',
            field=models.CharField(choices=[('요청대기', '요청대기'), ('요청승인', '요청승인'), ('요청거절', '요청거절')], default='요청대기', max_length=50),
        ),
        migrations.AlterField(
            model_name='messageitem',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TimeBank_app.post', verbose_name='원글'),
        ),
        migrations.AlterField(
            model_name='post',
            name='applicants',
            field=models.ManyToManyField(blank=True, related_name='applier', to=settings.AUTH_USER_MODEL),
        ),
    ]
