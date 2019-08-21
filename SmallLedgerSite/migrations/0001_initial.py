# Generated by Django 2.2.4 on 2019-08-08 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('profitmargin', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('serialnumber', models.CharField(max_length=100)),
                ('extrainformation', models.TextField(blank=True, null=True)),
                ('boughtprice', models.DecimalField(decimal_places=2, max_digits=7)),
                ('soldPrice', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
                ('boughtDate', models.DateField()),
                ('soldDate', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExtraCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('information', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SmallLedgerSite.Item')),
            ],
        ),
    ]
