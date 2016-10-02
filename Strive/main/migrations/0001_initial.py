# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 00:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('prizes', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_matchup', models.IntegerField(default=0)),
                ('a_won_true', models.BooleanField()),
                ('company_match_a', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_match_a', to='main.Company')),
                ('company_match_b', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_match_b', to='main.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(verbose_name='date started')),
                ('tags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('vote_to_company_a', models.BooleanField()),
                ('company_match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Match')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Tournament'),
        ),
        migrations.AddField(
            model_name='company',
            name='tags',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Tag'),
        ),
    ]
