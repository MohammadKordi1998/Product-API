# Generated by Django 4.1.6 on 2023-02-17 12:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Roles', '0004_rename_created_roles_datetime_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessPage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('page', models.CharField(max_length=1000)),
                ('method', models.CharField(max_length=1000)),
                ('role', models.ManyToManyField(to='Roles.roles')),
            ],
        ),
    ]