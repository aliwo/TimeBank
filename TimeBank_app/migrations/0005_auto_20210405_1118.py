# Generated by Django 3.1.7 on 2021-04-05 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TimeBank_app', '0004_auto_20210405_1113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messageitem',
            old_name='user',
            new_name='author',
        ),
    ]
