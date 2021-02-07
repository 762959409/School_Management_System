# Generated by Django 3.0.7 on 2021-02-06 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0014_auto_20210204_0621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monday', to='classes.Subject')),
                ('related_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Class')),
                ('sunday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sunday', to='classes.Subject')),
                ('thursday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thursday', to='classes.Subject')),
                ('tuesday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tuesday', to='classes.Subject')),
                ('wednesay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wednesay', to='classes.Subject')),
            ],
        ),
    ]
