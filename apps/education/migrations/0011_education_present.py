# Generated by Django 2.2.5 on 2019-10-02 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0010_auto_20191002_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='present',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
