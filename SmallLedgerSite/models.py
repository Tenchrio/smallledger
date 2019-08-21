from django.db import models
from django.utils.timezone import now

#Category field with a desired profit margin, default zero, a function should be made to set all
class Category(models.Model):
    name = models.CharField(max_length=200)
    profitmargin = models.DecimalField(max_digits=5,decimal_places=2,default=0)

    def __str__(self):
        return "%s" % (self.name)
    
#The Brand of the item, a seperate import function can be made for this but I am still unsure about the Database type
class Brand(models.Model):
    name = models.CharField(max_length=200)

#The bread and butter, the item class is where it all comes together
#I would have split it into Item and ItemSold but considering the use case of this app 
#it would have made it more annoying for the user, 
#perhaps if I can find a database with Guitar brands and their products I will (but Google and DDG have nothing)
class Item(models.Model):
    image = models.ImageField(upload_to="images/",null=True,blank=True)
    name = models.CharField(max_length=200)
    #Serial numbers can include alphanumeric values like 123456B, go to wikipedia if you don't believe me
    serialnumber = models.CharField(max_length=100,null=True,blank=True)
    extrainformation = models.TextField(null=True, blank=True)
    boughtprice = models.DecimalField(max_digits=7,decimal_places=2)
    soldprice = models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    #Not putting this on auto_now, perfectly possible for something to be added a day after
    boughtdate = models.DateField(default=now)
    solddate = models.DateField(null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    ownusage = models.BooleanField(default=False)

    def CalculateProfit(self):
        profit = self.soldprice - (self.boughtprice + self.CalculateAddedCost())
        return profit
    
    def CalculateAddedCost(self):
        cost = 0
        for e in self.extracost_set.all():
            cost += e.cost
        return cost

    
    def CalculateSuggestedSalesPrice(self):
        addcost = 0
        costquerry = self.extracost_set.all()
        for entry in costquerry:
            addcost += entry.cost
        totalcost = self.boughtprice + addcost
        endprice = totalcost * (1 + (self.category.profitmargin / 100))
        endprice = round(endprice,2)
        return endprice

#Potential extra costs, all fields are obviously required
#Due to convential database storage of FK (cant point to an object that does not exist,
#the item object must be created first
class ExtraCost(models.Model):
    information = models.TextField()
    cost = models.DecimalField(max_digits=5,decimal_places=2)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
