# Generated by Django 4.2.2 on 2023-09-06 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minelog', '0009_exam_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='examq',
            name='opt1id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='examq',
            name='opt2id',
            field=models.IntegerField(null=True),
        ),
    ]