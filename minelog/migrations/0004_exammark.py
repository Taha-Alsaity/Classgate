# Generated by Django 4.2.2 on 2023-07-20 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minelog', '0003_alter_students_school'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamMark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('exam_name', models.CharField(max_length=100)),
                ('Mark', models.IntegerField()),
            ],
        ),
    ]
