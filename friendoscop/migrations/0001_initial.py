# Generated by Django 5.1.4 on 2025-01-10 20:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Cursus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_field', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('birth_date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('home_phone_number', models.CharField(max_length=10)),
                ('cell_phone_number', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=64)),
                ('friends', models.ManyToManyField(to='friendoscop.person')),
                ('faculty', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='friendoscop.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('publication_date', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='friendoscop.person')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='friendoscop.person')),
                ('office', models.CharField(max_length=30)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='friendoscop.campus')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='friendoscop.job')),
            ],
            bases=('friendoscop.person',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='friendoscop.person')),
                ('year', models.IntegerField()),
                ('cursus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='friendoscop.cursus')),
            ],
            bases=('friendoscop.person',),
        ),
    ]
