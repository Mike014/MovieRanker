# Generated by Django 5.1.4 on 2024-12-30 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='overview',
            field=models.TextField(default=''),
        ),
    ]
