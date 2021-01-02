from django import forms
from .models import Album, Artist

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = "__all__"

class AlbumForm(forms.ModelForm):
    release_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Album
        fields = "__all__"
