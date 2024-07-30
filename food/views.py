from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
# from django.template import loader
from django.shortcuts import render ,redirect
from .forms import Item_form

# Create your views here.
def index(request):
    item_list=Item.objects.all()
    # template=loader.get_template('food/index.html') this can be simply achieved by render from dajngo.shortcuts
    context={
        'item_list':item_list,
    }
    return render(request,'food/index.html',context)
    # return HttpResponse(template.render(context,request))

def item(request):
    return HttpResponse(f"<h1>items </h1>")

def detail(request,item_id):
    item=Item.objects.get(pk=item_id)
    context={
        'item':item,
    }
    return render(request,'food/detail.html',context)

def create_item(request):
    form=Item_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item-form.html',{'form':form})

def update_item(request,id):
    item=Item.objects.get(id=id)
    form=Item_form(request.POST or None ,instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item-form.html',{'form':form,'item':item})

def delete_item(request,id):
    item=Item.objects.get(id=id)
    if request.method=="POST":
        item.delete()
        return redirect('food:index')
    return render(request,'food/delete-item.html',{'item':item})
    

