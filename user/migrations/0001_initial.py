# Generated by Django 3.1.7 on 2021-04-08 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstUser', models.CharField(default='', max_length=100)),
                ('secondUser', models.CharField(default='', max_length=100)),
                ('met', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MatchLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstUser', models.CharField(default='', max_length=100)),
                ('secondUser', models.CharField(default='', max_length=100)),
                ('url', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=100)),
                ('name_text', models.CharField(default='', max_length=100)),
                ('bio_text', models.CharField(default='', max_length=500)),
                ('age', models.IntegerField(default=18)),
                ('grad_year', models.IntegerField(default=2021)),
                ('budget_lower', models.IntegerField(default=0)),
                ('budget_upper', models.IntegerField(default=800)),
                ('noise_level', models.IntegerField(default=5)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other/Prefer not to say')], default='O', max_length=100)),
                ('personality', models.CharField(choices=[('I', 'Introvert'), ('E', 'Extrovert')], default='I', max_length=100)),
                ('location', models.CharField(default='', max_length=1000)),
                ('car', models.CharField(choices=[('Y', 'Have a car'), ('N', 'Do not have a car')], default='N', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
            ],
        ),
    ]
