# Generated by Django 4.0 on 2022-01-01 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]