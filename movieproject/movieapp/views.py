from django.http import HttpResponse
from django.shortcuts import render, redirect

from .form import MovieForm
from . models import Movie

# Create your views here.


def index(request):
    movie = Movie.objects.all()
    context={
        'movie_list': movie
    }
    return render(request,'index.html', context)


def detail(request,movie_id):
    # return HttpResponse("this movie is " % movie_id)
    movie = Movie.objects.get(id = movie_id)
    return render(request,"detail.html",{'movie':movie})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        desc = request.POST.get('desc','')
        year = request.POST.get('year','')
        image= request.FILES.get('image')
        movie = Movie(name=name,desc=desc,year=year,image=image)
        movie.save()
    return render(request,"add.html")


def update(request, movieid):
    movie = Movie.objects.get(id=movieid)
    form=MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        return redirect('index.html')
    return render(request, "edit.html", {'form': form, 'movie': movie})


def delete(request,movieid):
    if request.method == 'POST':
        movie = Movie.objects.get(id=movieid)
        movie.delete()
        return redirect('index.html')
    return render(request,'delete.html')

