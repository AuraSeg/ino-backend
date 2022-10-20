# Generated by Django 4.1.2 on 2022-10-19 20:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('due_date', models.DateField(default=datetime.date.today)),
                ('completion_status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('function', models.CharField(max_length=500, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('milestone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='milestones.milestone')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='milestones.team')),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_leader', models.BooleanField(default=False)),
                ('is_member', models.BooleanField(default=False)),
                ('team_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='milestones.teammember')),
            ],
        ),
        migrations.AddField(
            model_name='milestone',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='milestones.team'),
        ),
    ]