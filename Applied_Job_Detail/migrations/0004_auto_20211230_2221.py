# Generated by Django 3.2.9 on 2021-12-30 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Applied_Job_Detail', '0003_auto_20211230_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_detail',
            name='jobid',
            field=models.CharField(default='0', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='company_detail',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
