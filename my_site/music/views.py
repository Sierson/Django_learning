from django.shortcuts import render
from .forms import MusicianForm, AlbumForm
from .models import Artist, Album

# Create your views here.
def home(request):
    artists = Artist.objects.order_by('name')
    context = {'artists': artists}
    return render(request, 'music.html', context=context)

def add_artist(request):
    form = MusicianForm()
    context = {'MusicianForm': form}

    if request.method == "POST":
        form = MusicianForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

    return render(request, 'add_artist.html', context=context)

def add_album(request):
    form = AlbumForm()
    context = {'AlbumForm': form}

    if request.method == "POST":
        form = AlbumForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

    return render(request, 'add_album.html', context=context)

def album_list(request):
    albums = Album.objects.all()
    context = {'albums': albums}
    return render(request, 'album_list.html', context=context)

def artist_info(request, artist_id):
    artist = Artist.objects.get(pk=artist_id)
    context = {'artist': artist}
    return render(request, 'artist_info.html', context=context)