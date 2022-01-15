# Generated by Django 4.0 on 2021-12-27 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_tag_prerequisite_learning'),
    ]

    operations = [
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('serial_number', models.IntegerField()),
                ('video_id', models.CharField(max_length=50)),
                ('is_preview', models.BooleanField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
    ]