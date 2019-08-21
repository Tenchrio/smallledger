from django.shortcuts import render, redirect
from .models import Item, Category,ExtraCost 
from .forms import CategoryForm, ItemForm, AddCostForm, SellForm, ItemEditForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required
def index(request):
    return render(request,'index.html')

@login_required
def stock(request):
    items = Item.objects.filter(soldprice = None).order_by('id')
    title="Stock"
    return render(request,'stock.html',{'title':title,'items':items})

@login_required
def sold(request):
    items = Item.objects.exclude(soldprice = None).order_by('id')
    title="Sold"
    return render(request,'sold.html',{'title':title,'items':items})

@login_required
def category(request):
    categories = Category.objects.all()
    title="Categories"
    return render(request,'category.html',{'title':title,'categories':categories})

@login_required
def addcategory(request):
    madeid=0
    if request.method== 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            newcat = Category(name=form.cleaned_data['name'],profitmargin=form.cleaned_data['profitmargin'])
            newcat.save()
            madeid=newcat.id
            return redirect(category)
    else:
        form = CategoryForm()    
    return render(request,'form.html',{'title':"Add Category",'form':form,'madeid':madeid,'succmessage':"added a category"})

@login_required
def additem(request):
    madeid=0
    if request.method == 'POST':
        form = ItemForm(request.POST,request.FILES)
        if form.is_valid():
            newitem = form.save()
            madeid = newitem.id
    else:
        form = ItemForm()
    return render(request,'form.html',{'title':"Add Item",'form':form,'madeid':madeid,'succmessage':"added an item"})

@login_required
def viewitem(request,item_id):
    obj = Item.objects.get(id=item_id)
    madeid=0
    return render(request,'iteminfo.html',{"object":obj})

@login_required
def addcost(request,item_id):
    relitem = Item.objects.get(id=item_id)
    madeid=0
    if request.method == 'POST':
        form = AddCostForm(request.POST)
        if form.is_valid():
            newcost = ExtraCost(information=form.cleaned_data['information'],cost=form.cleaned_data['cost'],item=relitem)
            newcost.save()
            madeid = newcost.id
            return redirect(viewitem,relitem.id)
    else:
        form= AddCostForm()
    return render(request,'form.html',{'form':form,'title':"Add item for " + relitem.name,'madeid':madeid,'succmessage':"added cost for " + relitem.name})

@login_required
def sellitem(request,item_id):
    relitem = Item.objects.get(id=item_id)
    madeid=0
    if request.method == 'POST':
        form = SellForm(request.POST)
        if form.is_valid():
            relitem.soldprice = form.cleaned_data['soldprice']
            relitem.solddate = form.cleaned_data['solddate']
            relitem.save()
            form = None
            madeid = relitem.id
    else:
        form=SellForm()
    return render(request,'form.html',{'form':form,'title':"Sell item " + relitem.name,'madeid':madeid,'succmessage':' sold item with name ' + relitem.name})

@login_required
def editcategory(request,category_id):
    ecat = Category.objects.get(id=category_id)
    madeid=0
    if request.method == 'POST':
        form = CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            ecat.name = form.cleaned_data['name']
            ecat.profitmargin = form.cleaned_data['profitmargin']
            ecat.save()
            madeid = ecat.id
    else:
        form = CategoryForm()
        form.fields['name'].initial = ecat.name
        form.fields['profitmargin'].initial = ecat.profitmargin
    return render(request,'form.html',{'form':form,'title':"Edit category",'madeid':madeid,'succmessage':' edited the category '})

@login_required
def deletecost(request, cost_id):
    cost = ExtraCost.objects.get(id=cost_id)
    itemid = cost.item.id
    if request.method == 'POST':    
        cost.delete()
    return redirect(viewitem,itemid)

@login_required
def edititem(request,item_id):
    relitem = Item.objects.get(id=item_id)
    madeid=0
    if request.method == "POST":
        form = ItemEditForm(request.POST,request.FILES,instance=relitem)
        if form.is_valid():
            form.save()
            madeid=relitem.id
            return redirect(viewitem, item_id)
    else:
        form = ItemEditForm(instance=relitem)
    return render(request,'form.html',{'form':form,'title':"Edit Item",'madeid':madeid,'succmessage':" edited the item "})

@login_required
def deleteitem(request,item_id):
    relitem = Item.objects.get(id=item_id)
    if request.method == 'POST':
        relitem.delete()
    return redirect(stock)

@login_required
def viewstats(request):
    return render(request,'statistics.html')
