# Generated by Django 2.2.1 on 2019-12-16 10:46

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QqMsg',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('source', models.CharField(max_length=50)),
                ('msg_id', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=25)),
                ('qq', models.CharField(max_length=25)),
                ('gc', models.CharField(max_length=25)),
                ('gn', models.CharField(max_length=255)),
                ('owner', models.CharField(max_length=25)),
                ('nick', models.CharField(max_length=255)),
                ('l_nick', models.TextField()),
                ('phone', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=25)),
                ('occupation', models.CharField(max_length=25)),
                ('avatar', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=25)),
                ('image', models.CharField(max_length=255)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'QQ消息',
                'verbose_name_plural': 'QQ消息',
                'db_table': 'qqmsg',
            },
        ),
    ]
