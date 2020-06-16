# Generated by Django 3.0.4 on 2020-06-16 15:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_task_adjunto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='adjunto',
            field=models.FileField(blank=True, null=True, upload_to='adjuntos', validators=[django.core.validators.FileExtensionValidator(['json', 'csv'])]),
        ),
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateField(default='2020-06-16'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(default='2020-06-16'),
        ),
    ]
