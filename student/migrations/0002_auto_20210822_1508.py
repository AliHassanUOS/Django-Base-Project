# Generated by Django 3.2.6 on 2021-08-22 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='just_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.BooleanField(blank=True),
        ),
    ]