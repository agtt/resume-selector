# Generated by Django 2.2.5 on 2019-10-02 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0009_university_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='chapter',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Chapter'),
        ),
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Degree'),
        ),
    ]