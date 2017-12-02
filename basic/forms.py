from django import forms
from .models import *

# author book album song news message Feedback music movie

class FeedbackForm(forms.ModelForm):
    suggestions = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Feedback
        fields = ['name', 'suggestions', 'email', 'phone_no']

class MusicForm(forms.ModelForm):
    class Meta:
        model=music
        fields = ['songs_name', 'songs_singer', 'category', 'songs_file', 'tag']

class MovieForm(forms.ModelForm):
    class Meta:
        model=movie
        fields = ['movie_name', 'movie_file', 'movie_director','category', 'tag']

class AuthorForm(forms.ModelForm):
    class Meta:
        model=author
        fields = ['author_name', 'tag']

class BookForm(forms.ModelForm):
    class Meta:
        model=book
        fields = ['book_name','book_genre', 'author', 'tag']

class AlbumForm(forms.ModelForm):
    class Meta:
        model=album
        fields = ['album_name','album_genre', 'tag']

class NewsForm(forms.ModelForm):
    class Meta:
        model=news
        fields = ['news_name','news_link', 'tag']

class DateInput(forms.DateInput):
    input_type = 'date'

class MessageForm(forms.ModelForm):
    message_text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model=message
        fields = [ 'reciever', 'message_text']
