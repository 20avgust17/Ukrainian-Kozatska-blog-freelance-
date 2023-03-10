# Generated by Django 4.1.5 on 2023-01-14 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Имя')),
                ('email', models.CharField(blank=True, max_length=50, verbose_name='Почта')),
                ('phone', models.CharField(blank=True, max_length=30, verbose_name='Телефон')),
                ('content', models.TextField(blank=True, max_length=500, verbose_name='Наполнение')),
            ],
        ),
    ]
