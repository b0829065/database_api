# Generated by Django 3.2.4 on 2021-06-22 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_auto_20210622_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Numbers_room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=45)),
                ('room_id', models.CharField(max_length=45)),
            ],
        ),
    ]
