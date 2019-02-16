# Generated by Django 2.1.5 on 2019-01-18 23:23

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
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=150)),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='end date')),
                ('description', models.TextField(default=None, verbose_name='description')),
                ('link', models.URLField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('languages', models.CharField(choices=[('TR', 'Turkish'), ('EN', 'English')], max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-end_date'],
            },
        ),
    ]
