# Generated by Django 2.2.7 on 2019-12-12 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='email',
            field=models.CharField(max_length=40),
        ),
    ]
