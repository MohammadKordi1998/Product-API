# Generated by Django 4.1.6 on 2023-02-17 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Access_Page', '0006_alter_accesspage_method_alter_accesspage_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesspage',
            name='method',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='accesspage',
            name='page',
            field=models.CharField(max_length=1000),
        ),
    ]
