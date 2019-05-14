from django.shortcuts import render, redirect, HttpResponse
from login_page.forms import RegistrationForm, Loginform
from django.contrib.auth import authenticate, login
from thread.models import Post, Post_reply
from django.db.models import Count

def index(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'login_page\Home.html',{'posts':posts})

def index_date(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'login_page\Home_date.html', {'posts': posts})

def index_replies(request):
    posts = Post.objects.all().annotate(reply_count=Count('comments')).order_by('-reply_count')
    return render(request, 'login_page\Home_reply.html', {'posts': posts})

def index_unanswered(request):
    posts=Post.objects.filter(comments__isnull=True)
    return render(request, 'login_page\Home_unans.html', {'posts': posts})

def index_trending(request):
    posts = Post.objects.all().annotate(reply_count=Count('comments')).order_by('-reply_count')
    return render(request, 'login_page\Home_trend.html', {'posts': posts})

def index_categories(request):
    posts = Post.objects.all().order_by('-category')
    return render(request, 'login_page\Home_Cate.html', {'posts': posts})

def logout(request):
    return render(request, 'login_page\Login.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/Home/Profile')
        else:
            form=Loginform()
            m1="Invalid Credentials !"
            m2="Please Enter A Valid Username And Password"
            return render(request, 'login_page\Login.html',{ 'm1':m1, 'm2':m2, 'form':form})
    else:
        form = Loginform()
        m1="Please Enter Your Credentials. "
        m2="Remember Passwords Are Case Sensitive"
        return render(request, 'login_page\Login.html', {'form': form,'m2':m2, 'm1':m1})


def profile(request):
    if request.user.is_authenticated:
        user_posts=Post.objects.filter(user=request.user).order_by('-date')
        recent_posts = user_posts[:3]
        user_answers=Post_reply.objects.filter(user=request.user).order_by('-date')
        recent_answers = user_answers[:3]
        args = {'user_posts':user_posts, 'user_answers':user_answers, 'recent_posts':recent_posts, 'recent_answers':recent_answers}
        return render(request, 'login_page\Profile.html', args)
    else:
        return render(request, 'login_page\Profile.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            form = Loginform()
            m1='Success'
            m2='You Have Been Registered Successfully, You can Login now,'
            return render(request,'login_page\Login.html',{'m1':m1, 'm2':m2, 'form':form})
        else:
            form = RegistrationForm()
            m1 = "Could Not Register !"
            m2 = "Either you did'nt enter the fields in specified format or your password did'nt match"
            args={'m1': m1, 'm2': m2, 'form': form,}
            return render(request, 'login_page\Register.html', args)
    else:
        m1 = "Register Here,"
        m2 = "Please Enter All Fields In Specified Format"
        form = RegistrationForm()
        return render(request, 'login_page\Register.html', {'form': form, 'm1': m1, 'm2': m2})


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        rel_posts = Post.objects.filter(post__icontains=q)
        return render(request, 'login_page\search_results.html', {'menu_item': rel_posts, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')
