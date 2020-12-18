from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', {})
def account(request):
    return render(request, 'account.html', {})
def settings(request):
    return render(request, 'settings.html', {})
def archive(request):
    return render(request, 'archive.html', {})
def lasvegas(request):
    return render(request, 'lasvegas.html', {})
def JejuIsland(request):
    return render(request, 'JejuIsland.html', {})
def single(request):
    return render(request, 'single.html', {})
def world(request):
    return render(request, 'world.html', {})
def korea(request):
    return render(request, 'korea.html', {})


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            #return redirect('world')
            return render(request, 'world.html', {})
    else:
        form = UserCreationForm()
    return render(request, 'singup.html', {'form': form})

from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password

def loginpage(request):
    return render(request, 'login.html', {})

def user_login(request):
    print(request.POST)
    form = LoginForm(request.POST)
    print(form.is_valid())

    if form.is_valid():
        data = form.cleaned_data
        user = authenticate(username=data['username'], password=data['password'])

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('world')

        else:
            return render(request, 'singup.html', {'form':form, 'error_msg' : '로그인 정보를 확인해주세요'})

    else:
        form = LoginForm
        return render(request, 'singup.html', {'form':form})

from .models import Post, Photo
from django.utils import timezone
...

def create(request):
    if(request.method == 'POST'):
        post = Post()
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.pub_date = timezone.datetime.now()
        post.user = request.user
        post.save()
        # name 속성이 imgs인 input 태그로부터 받은 파일들을 반복문을 통해 하나씩 가져온다
        for img in request.FILES.getlist('imgs'):
            # Photo 객체를 하나 생성한다.
            photo = Photo()
            # 외래키로 현재 생성한 Post의 기본키를 참조한다.
            photo.post = post
            # imgs로부터 가져온 이미지 파일 하나를 저장한다.
            photo.image = img
            # 데이터베이스에 저장
            photo.save()
        return HttpResponseRedirect('JejuIsland')
    else:
        return render(request, 'archive.html')