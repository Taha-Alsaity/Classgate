# Generated by Django 4.2.2 on 2023-09-05 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minelog', '0006_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='keyword',
            field=models.CharField(max_length=40, null=True),
        ),
    ]