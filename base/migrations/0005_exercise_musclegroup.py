# Generated by Django 3.2.8 on 2022-05-02 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20220502_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='muscleGroup',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]