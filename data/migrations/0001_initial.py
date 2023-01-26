# Generated by Django 4.1.2 on 2023-01-24 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invetory',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Item_Name', models.CharField(max_length=200)),
                ('Barcode', models.CharField(max_length=200)),
                ('MRP', models.FloatField()),
                ('Rate_A', models.FloatField()),
                ('Rate_B', models.FloatField()),
                ('Rate_C', models.FloatField()),
                ('WS_price', models.FloatField()),
                ('Last_Used', models.DateTimeField(blank=True)),
                ('Available_Stock', models.FloatField()),
                ('HSN', models.CharField(blank=True, max_length=200)),
                ('Tax_Percentage', models.FloatField(default=0.0)),
                ('Discount_Percentage', models.FloatField(default=0.0)),
                ('Low_Stock_Quantity', models.FloatField(default=0.0)),
                ('Expiry_Date', models.DateField(blank=True)),
                ('Description', models.TextField(blank=True)),
                ('Total_Sold', models.FloatField()),
                ('Brand_Name', models.CharField(max_length=500)),
                ('Supplier_Name', models.CharField(max_length=500)),
                ('Full_Bin_Qty', models.FloatField(default=0.0)),
                ('Managed_Bin', models.BooleanField(default=False)),
                ('Image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
