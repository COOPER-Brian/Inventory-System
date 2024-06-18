from django.db import models

# Create your models here.
      
     #field name and their characteristics

class Inventory(models.Model):
     name = models.CharField(max_length=250,null=False,blank=False)
     cost_per_item = models.DecimalField(max_digits=19, decimal_places=2,null=False,blank=False)
     quantity_in_stock = models.IntegerField(null=False,blank=False)
     quantity_sold = models.IntegerField(null=False,blank=False)
     sales = models.DecimalField(max_digits=19,decimal_places=2,null=False,blank=False)
     stock_Date = models.DateField(auto_now_add=True)
     last_sales_date = models.DateField(auto_now=True)
     

     def __str__(self):
         return self.name  # Return the name field for string representation
    
