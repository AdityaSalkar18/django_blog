# Generated by Django 4.1.5 on 2023-03-30 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_alter_profile_pimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pimage',
            field=models.ImageField(blank=True, default='', null=True, upload_to='pimages/'),
        ),
    ]