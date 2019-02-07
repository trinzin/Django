# Generated by Django 2.1.5 on 2019-02-05 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('price', models.FloatField(default=0)),
                ('image', models.ImageField(upload_to='food_images/')),
                ('origin', models.CharField(max_length=200)),
                ('submission_date', models.DateTimeField()),
            ],
        ),
    ]
