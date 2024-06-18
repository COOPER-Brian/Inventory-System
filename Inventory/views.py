from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Inventory             #model name
from django.contrib.auth.decorators import login_required            #must be logged in to access this platform
from .forms import AddInventoryForm
# Create your views here.

@login_required          #for authentication
def inventory_list(request):          
    inventories = Inventory.objects.all()
    #providing a title in a context using a dictionary.   Context help in pasing data from views to templates
    context = {
        "title": "Inventory List",
        "inventories": inventories
    
    }
    return render(request, "Inventor/inventory_list.html", context=context)     # folder name Inventor and has file index.....# Context used to provide a title
    #return render(request, 'Inventor/inventory_list.html', {'inventories': inventories}) #context=context)
 
@login_required
                                                                       
def per_product_view(request,pk):
    inventory = get_object_or_404(Inventory,pk=pk)     
    context = {
        'inventory': inventory
    }   
    #return  render (request, "inventor/per_product.html", context=context) 
    return  render (request, 'Inventor/per_product.html', {'inventory': inventory}) 

@login_required
def add_product(request):
    if request.method == "POST":
        add_form = AddInventoryForm(data=request.POST)
        if add_form.is_valid():
            new_inventory = add_form.save(commit=False)
            new_inventory.sales = float(add_form.cleaned_data['cost_per_item']) * float(add_form.cleaned_data['quantity_sold'])
            new_inventory.save()
            return redirect("/Inventory/")
            #return HttpResponse('Product added successfully!')

        else:
            add_form = AddInventoryForm()
        
        return render(request, "Inventor/inventory_add.html",{"form": add_form})
                                                     