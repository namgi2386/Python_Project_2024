from django.shortcuts import render , redirect , get_object_or_404
from .models import Movie
from .forms import MovieForm
from django.views.decorators.http import require_http_methods, require_safe

@require_safe
def index(request):
    movies = Movie.objects.all().order_by('-point')
    context = {
        'movies': movies,
    }
    return render(request , 'movies/index.html' , context)

@require_safe
def detail(request , pk):
    movies = get_object_or_404(Movie,pk=pk)
    context = {
        'movie': movies,
    }
    return render(request , 'movies/detail.html' , context)

@require_safe
def delete(request , pk):
    movies = Movie.objects.get(pk=pk)
    movies.delete()
    return redirect('movies:index')

@require_http_methods(["GET","POST"])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST ,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request , 'movies/create.html' , context)

@require_http_methods(["GET","POST"])
def update(request , pk):
    movies = Movie.objects.get(pk=pk)   
    if request.method == 'POST':
        form = MovieForm(request.POST ,files=request.FILES ,  instance=movies)
        if form.is_valid():
            movies = form.save()
            return redirect('movies:detail',movies.pk)
    else:
        form = MovieForm(instance=movies)
    context = {
        'movies':movies,
        'form':form,
    }
    return render(request, 'movies/update.html' , context)



