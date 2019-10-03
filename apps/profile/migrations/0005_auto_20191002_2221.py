# Generated by Django 2.2.5 on 2019-10-02 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20190209_2008'),
        ('profile', '0004_auto_20191002_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='background',
            field=models.ImageField(blank=True, upload_to='userprofiles2/background', verbose_name='Background'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='industry',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='profile_industry', to='job.Industry'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='languages',
            field=models.ManyToManyField(blank=True, related_name='profile_languages', to='language.Language'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='skills',
            field=models.ManyToManyField(blank=True, related_name='profile_skills', to='skill.Skill'),
        ),
    ]
