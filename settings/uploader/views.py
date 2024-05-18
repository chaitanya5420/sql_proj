from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *
import pandas as pd
# Create your views here.


def gallary(request):
    
    category = request.GET.get('category')
    if category == None:                # it checks if there is data in category model if there is no data then it will show all photos
        photos=Photo.objects.all()
    else:                                   
        photos=Photo.objects.filter(category__name=category)    #if there is data in category model then it will filterout that data on the name of category
    
    categories = Category.objects.all()
    context = {'categories':categories,'photos':photos}
    return render(request, 'gallary.html',context)



def add(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data= request.POST
        image =request.FILES.get('image') 
         
        if  data['category'] != 'none':                                #in it if there is data in category then it will fatch it using it's id
            category = Category.objects.get(id = data['category']) 
        elif data['new_category'] != '':
            category, created = Category.objects.get_or_create(name= data['new_category']) # it will check model category and the data in it if there id data then fatch it
                                                                                           #  if not then create new data in this case it will create new category
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
        return redirect('gallary')     # Redirect to some home page after deletion
    return redirect('photo', pk=pk)    # Redirect back to the view page if not a POST request


def base(request):
    form = FileUploadForm()
    files = UploadedFile.objects.all()
    context={'form':form,'files':files}
    return render(request,'base.html',context)


def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        form = FileUploadForm()
        files = UploadedFile.objects.all()
        context={'form':form,'files':files}
    return render(request, 'base.html', context)


# def view_files(request):
#     files = UploadedFile.objects.all()
#     return render(request, 'base.html', {'files': files})


def show_tables(request, file_id):
    file_obj = UploadedFile.objects.get(id=file_id)
    try:
        df = pd.read_csv(file_obj.file)
        tables = df.values.tolist()  # it converts each row of datafram into a list of lists means every index value has a list as it's value
        headings = df.columns.tolist()
        context = {'file_name': file_obj.name, 'tables': tables,'headings':headings}
        return render(request, 'table.html',context )
    except pd.errors.ParserError:
        error_message = "Error: The selected file is not a valid CSV file."
        return render(request, 'base.html', {'error_message': error_message})