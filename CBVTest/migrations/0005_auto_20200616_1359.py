# Generated by Django 2.2.6 on 2020-06-16 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CBVTest', '0004_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.IntegerField(choices=[[0, 'male'], [1, 'female']], default=0),
        ),
    ]
