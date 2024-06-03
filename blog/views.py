from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog.forms import PostForm, CommentForm, LoginForm
from blog.models import Post, Comment, Quiz, Question


# Create your views here.
def main_view(request):
    posts=Post.objects.all()
    for i in posts:
        print(i.title)
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = request.POST
            print(data)
            form = PostForm(data)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user

                post.save()
                post_id = post.id
                return redirect(f'/post/{post_id}/')
        else:
            form = PostForm()
        return render(
            request,
            'main_page.html',
            {'pst':posts,
             'form':form,
             'user':request.user},
        )
    else:
        return render(
            request,
            'main_page.html',
            {'pst':posts,
             'user':request.user
            },
        )

def post_view(request, pk):
    qs = Post.objects.filter(pk=pk)
    post = qs.first()
    c_qs = Comment.objects.filter(to_post=post)
    c_qs = c_qs.all()
    form = CommentForm()
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = request.POST
            print(data)
            form = CommentForm(data)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.to_post = post
                comment.save()
    return render(
        request,
        'one_post.html',
        {'post': post,
         'comments':c_qs,
         'form':form,
         'user':request.user,
         }
    )


def quiz_list(request,):
    quizes = Quiz.objects.all()
    return render(
        request,
        'quizes_list.html',
        {'quizes': quizes})
def quiz_detail(request, pk):
    quiz = Quiz.objects.filter(id=pk).first()

    quiz.questions = quiz.question_set.all()
    for question in quiz.questions:
        question.answers = question.answer_set.all()
    return render(request,
                  'quiz_detail.html',
                  {'quiz':quiz})

def login_view(request):
    form = LoginForm()
    # import ipdb
    # ipdb.set_trace() #ll n c
    if request.method == 'POST':
        login_name = request.POST['login']
        passw = request.POST['password']
        user = authenticate(request, username=login_name, password=passw)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            raise Exception('Такой пользователь не найден')

    return render(request,
                  'login.html',
                  {'form': form})

def register_view(request):
    form = LoginForm()
    # import ipdb
    # ipdb.set_trace() #ll n c
    if request.method == 'POST':
        login_name = request.POST['login']
        passw = request.POST['password']
        User = get_user_model()
        user_exists = User.objects.filter(username=login_name).exists()
        if not user_exists:
            p = User(username=login_name,)
            p.set_password(passw)
            p.save()
            login(request, p)
            return redirect('/')
        else:
            raise Exception('Такой пользователь не найден')

    return render(request,
                  'login.html',
                  {'form': form})

