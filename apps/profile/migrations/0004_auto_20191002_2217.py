# Generated by Django 2.2.5 on 2019-10-02 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0003_auto_20191002_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='languages',
            field=models.ManyToManyField(blank=True, related_name='user_languages', to='language.Language'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='skills',
            field=models.ManyToManyField(blank=True, related_name='user_skills', to='skill.Skill'),
        ),
    ]
