# Generated by Django 2.1.5 on 2019-02-09 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='industry',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_industry', to='job.Industry'),
        ),
        migrations.AlterField(
            model_name='job',
            name='section',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_section', to='job.Section'),
        ),
    ]
