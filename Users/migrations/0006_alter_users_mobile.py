# Generated by Django 4.1.6 on 2023-02-16 13:44

from django.db import migrations, models
import django_regex.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_users_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='mobile',
            field=models.CharField(max_length=11, unique=True, validators=[django_regex.validators.RegexValidator(message='The Mobile input value is Wrong', regex='^(\\+\\d{1,3})?,?\\s?\\d{8,13}')]),
        ),
    ]
