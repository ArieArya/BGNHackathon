# Generated by Django 3.1 on 2021-03-07 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatbotAnalytics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secretKey', models.TextField()),
                ('botName', models.TextField()),
                ('date', models.DateTimeField()),
                ('tag', models.TextField()),
                ('question', models.TextField()),
                ('response', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ChatbotDatabase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secretKey', models.TextField()),
                ('botName', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserDatabase',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.TextField()),
                ('password', models.TextField()),
                ('secretKey', models.TextField()),
            ],
        ),
    ]
