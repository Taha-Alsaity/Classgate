# Generated by Django 4.2.2 on 2023-12-13 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minelog', '0005_alter_students_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='password',
            field=models.IntegerField(),
        ),
    ]
