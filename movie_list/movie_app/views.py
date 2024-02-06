from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import MovieForm
from .models import Movie


# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movielst':movie
    }
    return render(request,'index.html' ,context)
def detail(request,movie_id):
    desc=Movie.objects.get(id=movie_id)
    return render(request ,"detail.html",{'movdes':desc})
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        img = request.FILES['image']
        movie1=Movie(name=name,dec=desc,year=year,img=img)
        movie1.save();
    return render(request,'add.html')
def edit(request,id):
    movie_new=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES,instance=movie_new)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'movie_db':movie_new,'form_db':form})
def delete(request,id):
    if request.method == 'POST':
        movie_new=Movie.objects.get(id=id)
        movie_new.delete()
        return redirect('/')
    return render(request,'delete.html')
