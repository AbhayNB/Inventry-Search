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
    def update_inventory(self):
        data = self
        data1 = [a.NewInv for a in [data]]
        ourdata = data1[0]
        d = pd.read_csv(ourdata)
        l = len(d)
        for a in range(l):
            p = Invetory()
            p.Item_Name = str(d['Item_Name'][a])
            p.Barcode = str(d['Barcode'][a])
            p.MRP = d['MRP'][a]
            p.Rate_A = d['Rate_A'][a]
            p.Rate_B = d['Rate_B'][a]
            p.Rate_C = d['Rate_C'][a]
            p.WS_price = d['WS_Price'][a]
            p.Last_Used = str(d['Last_Used'][a])
            p.Available_Stock = d['Available_Stock'][a]
            p.HSN = str(d['HSN'][a])
            p.Tax_Percentage = d['Tax_Percentage'][a]
            p.Discount_Percentage = d['Discount_Percentage'][a]
            p.Low_Stock_Quantity = d['Low_Stock_Quantity'][a]
            p.Expiry_Date = str(d['Expiry_Date'][a])
            p.Description = str(d['Description'][a])
            p.Total_Sold = d['Total_Sold'][a]
            p.Brand_Name = str(d['Brand_Name'][a])
            p.Supplier_Name = str(d['Supplier_Name'][a])
            p.Full_Bin_Qty = d['Full_Bin_Qty'][a]
            if d['Managed_Bin'][a] == 'FALSE':
                p.Managed_Bin = False
            else:
                p.Managed_Bin = True
            p.save()
    def __str__(self):
        return "New Inventory"
