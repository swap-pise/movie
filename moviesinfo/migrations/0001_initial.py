# Generated by Django 2.1.14 on 2019-11-28 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(max_length=100, verbose_name='mv_name')),
                ('aexprc', models.IntegerField(verbose_name='mv_name')),
                ('active', models.CharField(default='Y', max_length=100, verbose_name='active')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mvname', models.CharField(max_length=100, verbose_name='mv_name')),
                ('mvreviews', models.CharField(max_length=100, verbose_name='mv_reviews')),
                ('mvcategory', models.CharField(max_length=100, verbose_name='mv_category')),
                ('active', models.CharField(default='Y', max_length=100, verbose_name='active')),
            ],
        ),
        migrations.CreateModel(
            name='MovieActor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviesinfo.Actor')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviesinfo.Movie')),
            ],
        ),
    ]
