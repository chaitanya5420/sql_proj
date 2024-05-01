from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def base(request):
    return render(request, 'base.html')

def gallary(request):
    
    category = request.GET.get('category')
    if category ==None:
        photos=Photo.objects.all()
    else:
        photos=Photo.objects.filter(category__name=category)
    
    categories = Category.objects.all()
    context = {'categories':categories,'photos':photos}
    return render(request, 'gallary.html',context)

def add(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data= request.POST
        image =request.FILES.get('image') 
         
        if  data['category'] != 'none':
            category = Category.objects.get(id = data['category'])
        elif data['new_category'] != '':
            category, created = Category.objects.get_or_create(name= data['new_category'])
        else:
            category = None
           
        photo = Photo.objects.create(
            category=category,
            description=data['description'],
                image=image,
            )
        return redirect('gallary')
    
    
    context = {'categories':categories}
    return render(request, 'add.html',context)

def photo(request, pk):
    photos = Photo.objects.get(id=pk)
    categories = Category.objects.all()
    context = {'categories':categories,'photos':photos}
    return render(request, 'view.html',context)