# Generated by Django 4.2 on 2024-05-21 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_leisure'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]