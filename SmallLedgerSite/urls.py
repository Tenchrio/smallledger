from django.urls import path
from . import views

urlpatterns = [
                path('category',views.category,name='category'),
                path('category/<int:category_id>/edit',views.editcategory,name='editcategory'),
                path('',views.stock,name='stock'),
                path('sold',views.sold,name='sold'),
                path('category/add',views.addcategory,name='addcategory'),
                path('stock/add',views.additem,name='additem'),
                path('stock/view/<int:item_id>',views.viewitem,name="viewitem"),
                path('stock/view/<int:item_id>/addcost',views.addcost,name="addcosttoitem"),
                path('stock/view/<int:item_id>/sell',views.sellitem,name="sellitem"),
                path('stock/delcost/<int:cost_id>',views.deletecost,name="deletecost"),
                path('stock/edit/<int:item_id>',views.edititem,name="edititem"),
                path('stock/delete/<int:item_id>',views.deleteitem,name="deleteitem"),
                path('statistics',views.viewstats,name="viewstatistics")
                ]
