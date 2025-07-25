# Generated by Django 5.1.7 on 2025-07-22 02:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='link',
        ),
        migrations.AddField(
            model_name='project',
            name='appstore_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='figma_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='github_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='playstore_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='web_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='projects/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='projects.project')),
            ],
        ),
    ]
