# Generated by Django 4.1.4 on 2022-12-10 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.TextField(null=True),
        ),
    ]
