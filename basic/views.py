from django.shortcuts import render, redirect
from .models import *
from django.http.response import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import *
from django.utils.translation import ugettext as _
import datetime
from .feeds import NewsFeed
from django.db.models import Q


# author book album song news message Feedback music movie

def srch(q):
    q = str(q).upper()
    r = []
    for i in CustomUser.objects.all():
        if str(i.first_name).upper().find(q) is not -1:
            r.append(i)
    for i in Thing.objects.all():
        if str(i.tag).upper().find(q) is not -1:
            r.append(i)
    for i in message.objects.all():
        if str(i.message_text).upper().find(q) is not -1:
            r.append(i)
    for i in author.objects.all():
        if str(i.tag).upper().find(q) is not -1:
            r.append(i)
    for i in book.objects.all():
        if str(i.tag).upper().find(q) is not -1:
            r.append(i)
    for i in album.objects.all():
        if str(i.tag).upper().find(q) is not -1:
            r.append(i)
    for i in news.objects.all():
        if str(i.tag).upper().find(q) is not -1:
            r.append(i)
    for i in music.objects.all():
        if str(i.tag).upper().find(q) is not -1:
            r.append(i)
    for i in movie.objects.all():
        if str(i.tag).upper().find(q) is not -1:
            r.append(i)
    return r


@login_required(login_url='login:login')
def search(request):
    user = request.user
    if (request.method == 'POST'):
        result = srch(request.POST['query'])
        return render(request, 'form-search.html', {'get': result, 'value': request.POST['query'], "user":user,"struser": str(user) ,})
    else:
        return render(request, 'form-search.html', {"user":user,"struser": str(user) ,})


@login_required(login_url='login:login')
def home(request):
    if request.method == 'POST':
        new = CustomUser(usr=request.user, first_name=request.POST['first_name'],
                         last_name=request.POST['last_name'], image=request.FILES['image'],
                         tag=request.POST['first_name'])
        new.save()
        return render(request, 'startbootstrap-agency-gh-pages/index.html', {'user': new, 'struser':str(request.user)})
    else:
        for usr in CustomUser.objects.all():
            if str(usr.usr) == str(request.user):
                return render(request, 'startbootstrap-agency-gh-pages/index.html', {'user': usr.usr, 'struser':str(request.user)})


@login_required(login_url='login:login')
def logOut(request):
    logout(request)
    return redirect('login:login')


@login_required(login_url='login:login')
def feeds(request):
    form = FeedbackForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('basic:index')
    else:
        return render(request, 'startbootstrap-agency-gh-pages/index.html', {'message': 'feedback already exists'})

@login_required(login_url='login:login')
def addobject(request, id=-1):
    if request.path == '/basic/addmusic/':
        if request.method == 'POST':
            form = music(songs_name= request.POST['songs_name'],
                                   songs_file=request.FILES['songs_file'],
                                   category=request.POST['category'],
                                   posted_by=str(request.user),
                                   songs_singer=request.POST['songs_singer'],
                                   tag=request.POST['tag'],
                                   )
            form.save()
            return redirect('basic:index')
        else:
            form = MusicForm()
            return render(request, 'addmusic_html.html', context={'form': form, "struser":str(request.user)})
    elif request.path == '/basic/addmovie/':
        if request.method == 'POST':
            form = movie(movie_name=request.POST['movie_name'],
                                   posted_by=str(request.user),
                                   movie_director=request.POST['movie_director'],
                                   category=request.POST['category'],
                                   movie_file=request.FILES['movie_file'],
                                   tag=request.POST['tag'])
            form.save()
            return redirect('basic:index')
        else:
            form = MovieForm()
            return render(request, 'addmovie_html.html', context={'form': form, "struser":str(request.user)})
    elif request.path == '/basic/message/' + (id + "/" if id != -1 else ""):
        if request.method == 'POST':
            form = MessageForm(request.POST)
            if form.is_valid():
                mess = message()
                mess.sender = request.user
                mess.reciever = form.cleaned_data['reciever']
                mess.message_text = form.cleaned_data['message_text']
                mess.message_date = datetime.datetime.now()
                mess.save()
                return redirect('basic:index')
        elif id!=-1:
            form = MessageForm(data={'reciever': message.objects.get(pk=id).sender})
            return render(request, 'startbootstrap-agency-gh-pages/popup.html', {'form': form, "struser":str(request.user)})
        else:
            form = MessageForm()
            form.fields['reciever'].queryset = CustomUser.objects.filter(~Q(usr=request.user))
            return render(request, 'startbootstrap-agency-gh-pages/popup.html', {'form': form, "struser":str(request.user)})
    elif request.path == '/basic/addbook/':
        if request.method == 'POST':
            form = music(book_name= request.POST['book_name'],

                         book_genre=request.POST['book_genre'],
                                   posted_by=str(request.user),
                         author=request.POST['author'],
                                   tag=request.POST['tag'],
                                   )
            form.save()
            return redirect('basic:index')
        else:
            form = BookForm()
            return render(request, 'addbook.html', context={'form': form, "struser":str(request.user)})

@login_required(login_url='login:login')
def inbox(request):
    r = []
    for i in message.objects.all():
        if str(i.reciever) == str(request.user):
            r.append(i)
    return render(request, 'startbootstrap-agency-gh-pages/inbox.html', {'message': r, "user":request.user, "struser":str(request.user)})

def post(request):
    if request.method == 'POST':
        mess = message()
        mess.sender = request.user
        mess.reciever = CustomUser.objects.get(first_name='none')
        mess.message_text = request.POST['message_text']
        mess.message_date = datetime.datetime.now()
        mess.save()
        return redirect('basic:profile', user = request.user)

@login_required(login_url='login:login')
def delete(request, id):
    if request.path == '/basic/delmessage/' + id:
        mess = message.objects.get(pk=id)
        mess.delete()
        return redirect('basic:inbox')

@login_required(login_url='login:login')
def  profile(request, user):
    for i in CustomUser.objects.all():
        if str(i) == user:
            usr = i
            break
    else:
        raise Http404("User Does Not exist")
    post =[]
    for i in message.objects.all():
        if str(i.reciever) == "None":
            post.append(i)
    post.extend(music.objects.all())
    post.extend(movie.objects.all())
    return render(request, 'profile.html', { "user" : usr, "struser": str(usr) , "post" : post, "context": "Timeline"})

def like(request, content, id):
    if content == "music":
        obj = music.objects.get(id=id)
        if str(request.user) not in str(obj.liked_by).split(','):
            obj.liked_by = obj.liked_by + str(request.user) + ","
        obj.save()
        return redirect('basic:profile', user=request.user)

    elif content == "movie":
        obj = movie.objects.get(id=id)
        if str(request.user) not in str(obj.liked_by).split(','):
            obj.liked_by = obj.liked_by + str(request.user) + ","
        obj.save()
        return redirect('basic:profile', user=request.user)

    elif content == "messaages":
        obj = message.objects.get(id=id)
        if str(request.user) not in str(obj.liked_by).split(','):
            obj.liked_by = obj.liked_by + str(request.user) + ","
        obj.save()
        return redirect('basic:profile', user=request.user)

@login_required(login_url='login:login')
def adddetails(request):
    for usr in CustomUser.objects.all():
        if str(usr.usr) == str(request.user):
            return redirect('basic:index')
    return render(request, 'adddetails.html')

@login_required(login_url='login:login')
def comment(request, id):
    for i in CustomUser.objects.all():
        if str(i) ==  str(request.user):
            usr = i
            break
    else:
        raise Http404("User Does Not exist")
    mycomment  = feed.objects.filter(pk=id)
    return render(request, 'profile.html', {'user':usr,"struser": str(usr) , 'feed':mycomment})
