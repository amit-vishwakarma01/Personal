# Generated by Django 3.2.9 on 2021-12-30 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Applied_Job_Detail', '0005_delete_company_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='company_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('jobid', models.CharField(max_length=100)),
                ('compnay_name', models.CharField(max_length=100)),
                ('ctc', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]
