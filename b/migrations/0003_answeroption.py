# Generated by Django 5.1.5 on 2025-01-15 16:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b', '0002_subject_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='b.task')),
            ],
        ),
    ]
