# Generated by Django 2.2.7 on 2019-12-13 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20191212_1736'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flats',
            old_name='state',
            new_name='area',
        ),
        migrations.AlterField(
            model_name='realtor',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
