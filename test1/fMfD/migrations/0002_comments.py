# Generated by Django 2.2.4 on 2020-02-06 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fMfD', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=400)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
