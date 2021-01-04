# Generated by Django 3.0.7 on 2021-01-04 19:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('group', models.CharField(blank=True, choices=[('Sci', 'Science'), ('Hum', 'Humanities'), ('Bus', 'Business Studies')], max_length=30, null=True)),
                ('syllebus', models.FileField(max_length=200, null=True, upload_to='uploads/%Y/%m/')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_year', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(9999)])),
                ('subjective_marks', models.IntegerField()),
                ('subjective_pass_marks', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='subjective pass marks (in %)')),
                ('objective_marks', models.IntegerField()),
                ('objective_pass_marks', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='objective pass marks (in %)')),
                ('total_marks', models.IntegerField()),
                ('total_pass_marks', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='total pass marks (in %)')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('related_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Class')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='MarksSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjective_marks', models.DecimalField(decimal_places=2, max_digits=5)),
                ('objective_marks', models.DecimalField(decimal_places=2, max_digits=5)),
                ('total_marks', models.DecimalField(decimal_places=2, max_digits=5)),
                ('letter_grade', models.CharField(max_length=5)),
                ('exam', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.Exam')),
            ],
        ),
    ]
