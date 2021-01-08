# Generated by Django 3.0.7 on 2021-01-08 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_type', models.IntegerField(choices=[(0, 'General'), (1, 'Class Related')], null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=250, null=True)),
                ('description', models.TextField(null=True)),
                ('attachment', models.FileField(blank=True, max_length=200, null=True, upload_to='uploads/notice/%Y/%m/%d')),
            ],
        ),
    ]
