# Generated by Django 2.0.8 on 2020-08-12 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='education',
            fields=[
                ('id_cnt', models.AutoField(primary_key=True, serialize=False)),
                ('insti_name', models.CharField(default='', max_length=200)),
                ('s_year', models.IntegerField(default=0)),
                ('e_year', models.IntegerField(default=0)),
                ('degree', models.CharField(default='', max_length=150)),
                ('score', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='experience',
            fields=[
                ('id_cnt', models.AutoField(primary_key=True, serialize=False)),
                ('company', models.CharField(default='', max_length=150)),
                ('title', models.CharField(default='', max_length=200)),
                ('s_year', models.IntegerField(default=0)),
                ('e_year', models.IntegerField(default=0)),
                ('work', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('username', models.CharField(default='none', max_length=150, primary_key=True, serialize=False)),
                ('fname', models.CharField(default='', max_length=150)),
                ('lname', models.CharField(default='', max_length=150)),
                ('email', models.CharField(default='', max_length=150)),
                ('mob', models.CharField(default='', max_length=20)),
                ('link_in', models.CharField(default='', max_length=150)),
                ('github', models.CharField(default='', max_length=150)),
                ('lang', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id_cnt', models.AutoField(primary_key=True, serialize=False)),
                ('skill', models.CharField(default='', max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='experience',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Profile'),
        ),
        migrations.AddField(
            model_name='education',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Profile'),
        ),
    ]
