# Generated by Django 2.2.5 on 2019-10-02 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0011_education_present'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='activities',
            field=models.TextField(blank=True, verbose_name='Activities and Societies'),
        ),
        migrations.AddField(
            model_name='education',
            name='grade',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Grade'),
        ),
    ]