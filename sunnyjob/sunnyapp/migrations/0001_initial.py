# Generated by Django 5.0.6 on 2024-07-02 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jid', models.IntegerField()),
                ('jpdate', models.DateField()),
                ('jtitle', models.CharField(max_length=35)),
                ('cname', models.CharField(max_length=30)),
                ('edu', models.CharField(max_length=20)),
                ('loc', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('caddress', models.CharField(max_length=100)),
            ],
        ),
    ]
