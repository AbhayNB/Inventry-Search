from django.db import models
import pandas as pd
# Create your models here.
class Invetory(models.Model):
    ID=models.AutoField(primary_key=True)
    Item_Name=models.CharField(max_length=200)
    Barcode=models.CharField(max_length=200)
    MRP=models.FloatField()
    Rate_A=models.FloatField()
    Rate_B=models.FloatField()
    Rate_C=models.FloatField()
    WS_price=models.FloatField()
    Last_Used=models.CharField(max_length=200,blank=True)
    Available_Stock=models.FloatField()
    HSN=models.CharField(blank=True,max_length=200)
    Tax_Percentage=models.FloatField(default=0.0)
    Discount_Percentage=models.FloatField(default=0.0)
    Low_Stock_Quantity=models.FloatField(default=0.0)
    Expiry_Date=models.CharField(max_length=200,blank=True)
    Description=models.TextField(blank=True)
    Total_Sold=models.FloatField()
    Brand_Name=models.CharField(max_length=500)
    Supplier_Name=models.CharField(max_length=500)
    Full_Bin_Qty=models.FloatField(default=0.0)
    Managed_Bin=models.BooleanField(default=False)
    Image=models.ImageField(upload_to='media',blank=True)
    def __str__(self):
        return self.Item_Name
class UploadCSV(models.Model):
    NewInv=models.FileField(upload_to='media',blank=True)
    def __str__(self):
        return "New Inventory"
