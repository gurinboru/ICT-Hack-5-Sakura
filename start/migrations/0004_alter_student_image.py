# Generated by Django 4.1.4 on 2022-12-10 11:35

from django.db import migrations, models
import start.models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0003_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(default='default/photo_2022-12-10_14-15-39.jpg', upload_to=start.models.userPhoto_directory_path),
        ),
    ]