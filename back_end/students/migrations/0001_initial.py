# Generated by Django 3.0.7 on 2021-01-04 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('username', models.CharField(blank=True, max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1)),
                ('date_of_birth', models.DateField()),
                ('place_of_birth', models.CharField(max_length=30)),
                ('mother_name', models.CharField(max_length=100, verbose_name="Mother's name")),
                ('father_name', models.CharField(max_length=100, verbose_name="Father's name")),
                ('guardian_name', models.CharField(max_length=100, verbose_name="Guardian's name(applicaple if different from parents)")),
                ('present_address', models.TextField()),
                ('permanent_address', models.TextField()),
                ('email', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=11, verbose_name='Telephone no.')),
                ('emergency_telephone', models.CharField(max_length=11, verbose_name='Emergency telephone No.')),
                ('religion', models.CharField(max_length=30)),
                ('nationality', models.CharField(max_length=30)),
                ('previous_class', models.IntegerField()),
                ('previous_school', models.CharField(max_length=40)),
                ('tc_number', models.CharField(max_length=50, verbose_name='T.C no.')),
                ('date', models.DateField()),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('employed_guardian_name', models.CharField(max_length=50, verbose_name="Father/Mother's name")),
                ('student_signature', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Student's signature")),
                ('guardian_signature', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Guardian's signature")),
                ('headmaster_signature', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Headmaster/Principal's signature")),
                ('current_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Class')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
