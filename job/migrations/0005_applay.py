# Generated by Django 4.2.6 on 2023-10-09 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_job_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('cv', models.FileField(upload_to='applay/')),
                ('cover_letter', models.TextField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applay_job', to='job.job')),
            ],
        ),
    ]
