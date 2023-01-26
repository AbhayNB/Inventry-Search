from django.shortcuts import render,HttpResponse
import pandas as pd
from .models import Invetory
from .models import UploadCSV
# Create your views here.
def ShowInvetory(request):
    Idata=Invetory.objects.all()
    data=UploadCSV.objects.all()
    # fname=[a.name for a in fdata]
    # f_name_str="\n".join(fname)
    # return HttpResponse("Our faculty names are:\n>>"+f_name_str)
    Bar_query = request.GET.get('Barcode')
    # Teacher_query = request.GET.get('Teacher')
    # print(Department_query)
    if Bar_query != '' and Bar_query is not None:
        Idata = Idata.filter(Barcode=Bar_query)
        context={'data':Idata,'update':data}
    else:
        context={'data':[],'update':data}
    # if Teacher_query != '' and Teacher_query is not None:
    #     fdata = fdata.filter(name__icontains=Teacher_query)
    # context={'data':Idata}
    return render(request,'data/index.html',context)
def UpdateInv(request):
    data=UploadCSV.objects.all()
    data1=[a.NewInv for a in data]
    ourdata=data1[0]
    # d = pd.read_csv(ourdata)
    # l=len(d)
    # for a in range(l):
    #     p=Invetory()
    #     p.Item_Name=str(d['Item_Name'][a])
    #     p.Barcode=str(d['Barcode'][a])
    #     p.MRP=d['MRP'][a]
    #     p.Rate_A=d['Rate_A'][a]
    #     p.Rate_B=d['Rate_B'][a]
    #     p.Rate_C=d['Rate_C'][a]
    #     p.WS_price=d['WS_Price'][a]
    #     p.Last_Used=str(d['Last_Used'][a])
    #     p.Available_Stock=d['Available_Stock'][a]
    #     p.HSN=str(d['HSN'][a])
    #     p.Tax_Percentage=d['Tax_Percentage'][a]
    #     p.Discount_Percentage=d['Discount_Percentage'][a]
    #     p.Low_Stock_Quantity=d['Low_Stock_Quantity'][a]
    #     p.Expiry_Date=str(d['Expiry_Date'][a])
    #     p.Description=str(d['Description'][a])
    #     p.Total_Sold=d['Total_Sold'][a]
    #     p.Brand_Name=str(d['Brand_Name'][a])
    #     p.Supplier_Name=str(d['Supplier_Name'][a])
    #     p.Full_Bin_Qty=d['Full_Bin_Qty'][a]
    #     if d['Managed_Bin'][a]=='FALSE':
    #         p.Managed_Bin=False
    #     else:
    #         p.Managed_Bin=True
    #     p.save()
    return render(request,'data/index.html')
def UpdateI(request):
    data=UploadCSV.objects.all()
    data1=[a.NewInv for a in data]
    ourdata=data1[0]
    d = pd.read_csv(ourdata)
    l=len(d)
    for a in range(l):
        p=Invetory()
        p.Item_Name=str(d['Item_Name'][a])
        p.Barcode=str(d['Barcode'][a])
        p.MRP=d['MRP'][a]
        p.Rate_A=d['Rate_A'][a]
        p.Rate_B=d['Rate_B'][a]
        p.Rate_C=d['Rate_C'][a]
        p.WS_price=d['WS_Price'][a]
        p.Last_Used=str(d['Last_Used'][a])
        p.Available_Stock=d['Available_Stock'][a]
        p.HSN=str(d['HSN'][a])
        p.Tax_Percentage=d['Tax_Percentage'][a]
        p.Discount_Percentage=d['Discount_Percentage'][a]
        p.Low_Stock_Quantity=d['Low_Stock_Quantity'][a]
        p.Expiry_Date=str(d['Expiry_Date'][a])
        p.Description=str(d['Description'][a])
        p.Total_Sold=d['Total_Sold'][a]
        p.Brand_Name=str(d['Brand_Name'][a])
        p.Supplier_Name=str(d['Supplier_Name'][a])
        p.Full_Bin_Qty=d['Full_Bin_Qty'][a]
        if d['Managed_Bin'][a]=='FALSE':
            p.Managed_Bin=False
        else:
            p.Managed_Bin=True
        p.save()
    return render(request,'data/index.html')