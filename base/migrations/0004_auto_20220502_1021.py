# Generated by Django 3.2.8 on 2022-05-02 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='user',
        ),
        migrations.AddField(
            model_name='exercise',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
