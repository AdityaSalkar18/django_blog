# Generated by Django 4.1.5 on 2023-03-31 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_alter_profile_aboutme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='toauthor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.post'),
        ),
    ]
