from django.urls import path, include
from music import views

app_name = 'music'
urlpatterns = [
    path('', views.home, name='home'),
    path('add-artist/', views.add_artist, name='add_artist'),
    path('add-album/', views.add_album, name='add_album'),
    path('album-list/', views.album_list, name='album_list'),
    path('artist-info/<int:artist_id>', views.artist_info, name='artist_info'),
]
