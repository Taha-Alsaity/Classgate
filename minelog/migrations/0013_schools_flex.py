# Generated by Django 4.2.2 on 2024-03-23 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minelog', '0012_remove_content_arkeyword_remove_content_artitle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='schools',
            name='flex',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
