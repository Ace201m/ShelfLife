from django.db import models
from django.contrib.auth.admin import User


class Thing(models.Model):
    tag = models.CharField(max_length=1000)
    posted_by = models.CharField(max_length=1000, default="None")
    liked_by = models.CharField(max_length=1000, default="None")

    def __str__(self):
        return self.tag


class CustomUser(models.Model):
    usr = models.OneToOneField(User)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.FileField(default='static/icon.png')
    tag = models.CharField(max_length=1000)

    def __str__(self):
        return self.usr.username

class author(models.Model):
    author_name = models.CharField(max_length=100)
    tag = models.CharField(max_length=1000)
    posted_by = models.CharField(max_length=1000, default="None")
    liked_by = models.CharField(max_length=1000, default="None")
    content = models.CharField(max_length=100, default="author")

    def __str__(self):
     return self.author_name

book_cat=(('Thriller','Thriller'),('Love Story','Love Story'),('Suspense','Suspense'))
class book(models.Model):
    author= models.ForeignKey(author, on_delete= models.CASCADE)
    book_name = models.CharField(max_length=100)
    book_genre = models.CharField(max_length=100,choices=book_cat)
    tag = models.CharField(max_length=1000)
    posted_by = models.CharField(max_length=1000, default="None")
    liked_by = models.CharField(max_length=1000, default="None")
    content = models.CharField(max_length=100, default="book")

    def __str__(self):
        return self.book_name

class album(models.Model):
    album_name = models.CharField(max_length= 100)
    album_genre = models.CharField(max_length=100,null=True)
    posted_by = models.CharField(max_length=1000, default="None")
    tag = models.CharField(max_length=1000)
    liked_by = models.CharField(max_length=1000, default="None")
    content = models.CharField(max_length=100, default="album")

    def __str__(self):
        return self.album_name

class news(models.Model):
    news_name= models.CharField(max_length=100)
    news_link = models.CharField(max_length=1000)
    tag = models.CharField(max_length=1000)
    posted_by = models.CharField(max_length=1000, default="None")
    liked_by = models.CharField(max_length=1000, default="None")
    content = models.CharField(max_length=100, default="news")

    def __str__(self):
        return self.news_name

class message(models.Model):
    sender = models.ForeignKey(User)
    reciever = models.ForeignKey(CustomUser)
    message_text= models.CharField(max_length=1000)
    message_date= models.CharField(max_length=200)
    liked_by = models.CharField(max_length=1000, default="None")
    posted_by = models.CharField(max_length=1000, default="None")
    content = models.CharField(max_length=100, default="messaages")

    def __str__(self):
        return self.message_text

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default='example@example.com')
    phone_no = models.IntegerField(default='0')
    suggestions = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

cat=(('rock','rock'),('pop','pop'),('classical','classical'),('hardcore','hardcore'))

class music(models.Model):
    songs_name = models.CharField(max_length=100)
    posted_by = models.CharField(max_length=1000, default="None")
    songs_singer = models.CharField(max_length=100)
    category = models.CharField(max_length=100,choices=cat)
    songs_file = models.FileField()
    tag = models.CharField(max_length=1000)
    content = models.CharField(max_length=100, default="music")
    liked_by = models.CharField(max_length=1000, default="None")

    def __str__(self):
        return self.songs_name

mov_cat=(('romance','romance'),('drama','drama'),('comedy','comedy'),('fiction','fiction'))
class movie(models.Model):
    movie_name = models.CharField(max_length=100)
    posted_by = models.CharField(max_length=1000, default="None")
    movie_director = models.CharField(max_length=100)
    movie_file = models.FileField(default="None")
    liked_by = models.CharField(max_length=1000, default="None")
    content = models.CharField(max_length=100, default="movie")
    category = models.CharField(max_length=100,choices=mov_cat)
    tag = models.CharField(max_length=1000)

    def __str__(self):
        return self.movie_name

class feed(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    time = models.DateTimeField()

    def __str__(self):
        return self.title