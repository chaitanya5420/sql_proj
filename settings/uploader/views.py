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

def delete_photo(request, pk):
    photos = Photo.objects.get(id=pk)
    if request.method == 'POST':
        photos.delete()
        return redirect('gallary')  # Redirect to some other page after deletion
    return redirect('photo', pk=pk)  # Redirect back to the view page if not a POST request


def base(request):
    return render(request,'base.html')


def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view')
    else:
        form = FileUploadForm()
    return render(request, 'file.html', {'form': form})


def view_files(request):
    files = UploadedFile.objects.all()
    return render(request, 'base.html', {'files': files})


def show_tables(request, file_id):
    file_obj = UploadedFile.objects.get(id=file_id)
    try:
        df = pd.read_csv(file_obj.file)
        tables = df.values.tolist() 
        headings = df.columns.tolist()
        context = {'file_name': file_obj.name, 'tables': tables,'headings':headings}
        return render(request, 'table.html',context )
    except pd.errors.ParserError:
        error_message = "Error: The selected file is not a valid CSV file."
        return render(request, 'base.html', {'error_message': error_message})