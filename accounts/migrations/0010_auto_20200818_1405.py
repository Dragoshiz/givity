# Generated by Django 3.0.8 on 2020-08-18 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200818_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]