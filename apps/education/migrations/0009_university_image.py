# Generated by Django 2.2.5 on 2019-10-02 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0008_auto_20191002_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Logo'),
        ),
    ]