# Generated by Django 4.1.4 on 2022-12-10 23:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import start.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('INN', models.IntegerField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('definitions', models.TextField()),
                ('budjet', models.IntegerField()),
                ('dedlines', models.IntegerField()),
                ('positions', models.TextField()),
                ('techDocument', models.FileField(upload_to=start.models.usertechDocument_directory_path)),
                ('goalOfProject', models.TextField()),
                ('background', models.TextField()),
                ('result', models.TextField()),
                ('criterias', models.TextField()),
                ('tags', models.TextField(null=True)),
                ('contactPerson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='start.contactperson')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'db_table': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='StatusApproval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Согласовано', 'Согласовано'), ('На согласовании', 'На согласовании'), ('Отказано', 'Отказано')], max_length=300)),
            ],
            options={
                'verbose_name': 'StatusApproval',
                'verbose_name_plural': 'StatusApproval',
                'db_table': 'StatusApproval',
            },
        ),
        migrations.CreateModel(
            name='StatusProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Открыта', 'Открыта'), ('Закрыта', 'Закрыта'), ('Заморожена', 'Заморожена')], max_length=300)),
            ],
            options={
                'verbose_name': 'StatusProject',
                'verbose_name_plural': 'StatusProject',
                'db_table': 'StatusProject',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.TextField(null=True)),
                ('image', models.ImageField(default='default/photo_2022-12-10_14-15-39.jpg', upload_to=start.models.userPhoto_directory_path)),
                ('tags', models.TextField(null=True)),
                ('ISU', models.IntegerField(null=True)),
                ('CV', models.FileField(null=True, upload_to='')),
                ('education', models.TextField(null=True)),
                ('department', models.TextField(null=True)),
                ('hardskill_softskill', models.TextField(null=True)),
                ('experience', models.TextField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='start.project')),
                ('statusApproval', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='start.statusapproval')),
                ('students', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='start.student')),
            ],
        ),
        migrations.CreateModel(
            name='Rialto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('definitions', models.TextField()),
                ('presentation', models.FileField(upload_to=start.models.userpresentationDocument_directory_path)),
                ('investment', models.IntegerField()),
                ('dedline', models.DateField()),
                ('FCF', models.IntegerField()),
                ('status_approval', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='start.statusapproval')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start.student')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='id_status',
            field=models.ForeignKey(db_column='id_status', on_delete=django.db.models.deletion.DO_NOTHING, to='start.statusproject'),
        ),
        migrations.AddField(
            model_name='project',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='start.organization'),
        ),
        migrations.AddField(
            model_name='project',
            name='status_approval',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='start.statusapproval'),
        ),
        migrations.CreateModel(
            name='ApprovalPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.TextField()),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start.organization')),
                ('statusApproval', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='start.statusapproval')),
            ],
        ),
    ]