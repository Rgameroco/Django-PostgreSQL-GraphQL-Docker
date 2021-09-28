# Generated by Django 3.2.7 on 2021-09-27 02:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FieldWorker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('function', models.CharField(choices=[('1', 'Harvest'), ('2', 'Pruning'), ('3', 'Scouting'), ('4', 'Other')], max_length=1)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
