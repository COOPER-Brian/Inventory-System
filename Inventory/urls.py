from django.urls import path 
from .views import inventory_list,per_product_view,add_product


urlpatterns = [
   path("",inventory_list,name="inventory_list"),
   path("per_product/<int:pk>", per_product_view, name='per_product'),
   #path("per_product/<int:pk>/",per_product_view,name='per_product_view'),
   path("add_inventory/",add_product,name='add_inventory')

  
]
   



# Here i import path and index file from my inventor folder  and create a urls from my inventory app.