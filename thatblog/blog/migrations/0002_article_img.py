# Generated by Django 5.0.3 on 2024-04-08 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
