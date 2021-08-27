# Generated by Django 3.2 on 2021-06-12 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('skills', models.TextField(max_length=100)),
                ('about_you', models.TextField(max_length=100)),
            ],
        ),
    ]
