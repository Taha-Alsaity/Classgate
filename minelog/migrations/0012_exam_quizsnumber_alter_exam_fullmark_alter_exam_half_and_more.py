# Generated by Django 4.2.2 on 2023-09-09 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minelog', '0011_students_rule'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='quizsnumber',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='fullmark',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='exam',
            name='half',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='examq',
            name='qmark',
            field=models.FloatField(),
        ),
    ]
