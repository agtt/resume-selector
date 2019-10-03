# Generated by Django 2.2.5 on 2019-10-02 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0004_auto_20191002_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='level',
            field=models.IntegerField(choices=[(1, 1), (2, 1.5), (3, 2), (4, 2.5), (5, 3), (6, 3.5), (7, 4), (8, 4.5), (9, 5)], default=1, verbose_name='Proficiency'),
        ),
    ]
