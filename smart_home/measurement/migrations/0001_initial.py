# Generated by Django 4.0.3 on 2022-04-10 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='описание(необязательно)')),
            ],
            options={
                'verbose_name': 'датчик',
                'verbose_name_plural': 'датчики',
            },
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(verbose_name='температура')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата и время измерения')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='measurement.sensor', verbose_name='датчик')),
            ],
            options={
                'verbose_name': 'показание',
                'verbose_name_plural': 'показания',
            },
        ),
    ]
