# Generated by Django 4.0 on 2022-01-08 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='user_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.usercourse'),
        ),
    ]
