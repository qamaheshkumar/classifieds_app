# Generated by Django 3.0.3 on 2021-10-24 08:42

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('user_password', models.CharField(max_length=20)),
                ('user_email', models.CharField(max_length=40)),
                ('user_number', models.CharField(max_length=10)),
                ('is_admin', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Classified',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('images', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='E:\\Django_React\\adsfrontend\\src\\adsImages\\'), upload_to='')),
                ('state', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
                ('zip_code', models.IntegerField()),
                ('is_hide', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Classified', to='api.Category')),
                ('status_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Classified', to='api.Status')),
                ('users_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Classified', to='api.Users')),
            ],
        ),
    ]
