# Generated by Django 3.1.2 on 2020-11-07 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=200, null=True)),
                ('degree', models.CharField(max_length=5, null=True)),
                ('year_of_joining', models.IntegerField(null=True)),
                ('dob', models.CharField(max_length=10, null=True)),
                ('image', models.ImageField(default='profile_pics/dummy.png', null=True, upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
