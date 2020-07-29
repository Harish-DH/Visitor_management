# Generated by Django 3.0.7 on 2020-07-13 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='tag',
            field=models.ManyToManyField(blank=True, default='blank', null=True, to='basic.Tag'),
        ),
    ]
