# Generated by Django 2.2.5 on 2019-10-02 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0002_language_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='level',
            field=models.FloatField(choices=[(1, 1), (1.5, 1.5), (2, 2)], default=1, verbose_name='Proficiency'),
        ),
    ]
