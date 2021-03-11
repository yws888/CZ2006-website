# Generated by Django 3.1.7 on 2021-03-10 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HDBResaleFlat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monthOfSale', models.CharField(max_length=10)),
                ('town', models.CharField(max_length=150)),
                ('flatType', models.CharField(max_length=50)),
                ('blockNo', models.CharField(max_length=10)),
                ('streetName', models.CharField(max_length=150)),
                ('storeyRange', models.CharField(max_length=10)),
                ('floorArea', models.IntegerField()),
                ('flatModel', models.CharField(max_length=50)),
                ('leaseCommencementYear', models.IntegerField()),
                ('remainingLease', models.IntegerField()),
                ('resalePrice', models.IntegerField()),
            ],
        ),
    ]