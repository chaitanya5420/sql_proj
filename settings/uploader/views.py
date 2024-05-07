from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *
import pandas as pd
# Create your views here.


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



def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view')
    else:
        form = FileUploadForm()
    return render(request, 'file.html', {'form': form})

def base(request):
    return render(request,'base.html')


def view_files(request):
    files = UploadedFile.objects.all()
    file_tables = []
    
    for file_obj in files:
       
        try:
            df = pd.read_csv(file_obj.file)
            tables = df.columns.tolist()
            file_tables.append({'file_name': file_obj.file.name, 'tables': tables})
        except pd.errors.ParserError:
            # Handle the case where file is not a CSV or cannot be parsed
            pass
            
    return render(request, 'table.html', {'file_tables': file_tables})