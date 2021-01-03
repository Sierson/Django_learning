from django.urls import path, include
from music import views

app_name = 'music'
urlpatterns = [
    path('', views.home, name='home'),
    path('add-artist/', views.add_artist, name='add_artist'),
    path('add-album/', views.add_album, name='add_album'),
    path('album-list/', views.album_list, name='album_list'),
    path('edit-artist/<int:artist_id>/', views.edit_artist, name='edit_artist'),
    path('artist-info/<int:artist_id>/', views.artist_info, name='artist_info'),
    path('edit-album/<int:album_id>/', views.edit_album, name='edit_album'),
    path('delete-album/<int:album_id>/', views.delete_album, name='delete_album'),
    path('delete-artist/<int:artist_id>/', views.delete_artist, name='delete_artist'),
]
