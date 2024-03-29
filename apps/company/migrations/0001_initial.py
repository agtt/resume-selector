# Generated by Django 2.1.5 on 2019-02-12 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Company Name')),
                ('link', models.URLField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Logo')),
            ],
        ),
    ]
