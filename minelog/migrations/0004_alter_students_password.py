# Generated by Django 4.2.2 on 2023-12-13 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minelog', '0003_exam_teacher_alter_content_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
