# Generated by Django 2.2.5 on 2019-10-02 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_company_description'),
        ('experience', '0007_auto_20191002_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='position_sector',
        ),
        migrations.AddField(
            model_name='experience',
            name='industry',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='experience_industry', to='company.Company'),
            preserve_default=False,
        ),
    ]
