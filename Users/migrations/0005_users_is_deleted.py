# Generated by Django 4.1.6 on 2023-02-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_alter_users_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
