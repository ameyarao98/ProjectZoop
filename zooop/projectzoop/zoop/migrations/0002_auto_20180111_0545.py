# Generated by Django 2.0 on 2018-01-11 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
