# Generated by Django 3.1.5 on 2021-01-31 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.IntegerField()),
                ('isready', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'foods',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('jumlah', models.IntegerField()),
                ('foods', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.foods')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Pesanans',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=200, null=True)),
                ('nomeja', models.IntegerField()),
                ('keranjang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.users')),
            ],
            options={
                'db_table': 'pesanans',
            },
        ),
    ]
