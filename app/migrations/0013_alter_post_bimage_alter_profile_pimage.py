# Generated by Django 4.1.5 on 2023-03-29 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bimage',
            field=models.ImageField(default='', upload_to='bimages/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pimage',
            field=models.ImageField(blank=True, default='', null=True, upload_to='pimages/'),
        ),
    ]