# Generated by Django 5.0.3 on 2024-03-12 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ['last_name', 'first_name']},
        ),
    ]
