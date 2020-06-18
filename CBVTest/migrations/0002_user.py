# Generated by Django 2.2.6 on 2020-06-14 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CBVTest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pwd', models.CharField(max_length=20)),
                ('sex', models.IntegerField(choices=[['0', 'male'], ['1', 'femal']], default=0)),
                ('icon', models.ImageField(default='icon/default.jpeg', upload_to='icon')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
