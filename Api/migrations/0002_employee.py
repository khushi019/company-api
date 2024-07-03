# Generated by Django 5.0.6 on 2024-06-24 12:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('phone_no', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('about', models.TextField()),
                ('position', models.CharField(choices=[('Manager', 'manager'), ('Software Developer', 'SDE'), ('Python Developer', 'PDE'), ('Director', 'Director'), ('AI/ML Developer', 'AI/ML'), ('HR', 'HR'), ('Entrepreneur', 'EP'), ('Civil Engineer', 'CE'), ('Lawyer', 'Law'), ('Team Leader', 'TL'), ('Mechanical Engineer', 'ME'), ('Electronics or Electrical Engineer', 'ECE/EEE'), ('Accountant', 'CA'), ('Business Analyst', 'BA'), ('Data Analyst', 'DA'), ('Chief Executive Officer', 'CEO')], max_length=100)),
                ('date_of_joining', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.company')),
            ],
        ),
    ]
