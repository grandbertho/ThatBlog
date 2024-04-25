# views.py

from django.shortcuts import render, get_object_or_404, redirect
from random import sample
from .forms import ArticleForm
from .models import Article, Category
from django.contrib.auth.decorators import login_required

def home(request):
    categories = Category.objects.all()
    random_articles = sample(list(Article.objects.all()), 2)  # Change 6 to the desired number of random articles
    
    return render(request, 'blog/home.html', {'categories': categories, 'random_articles': random_articles})


# views.py
from django.shortcuts import render, get_object_or_404
from .models import Article, Comment
from .forms import CommentForm


def all_articles(request):
    articles = Article.objects.all()
    return render(request, 'blog/articles.html', {'articles': articles})

def articles_by_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    articles = Article.objects.filter(category=category)
    allcategory = Category.objects.all()
    return render(request, 'blog/articles_by_category.html', {'category': category, 'articles': articles, 'allcategory':allcategory})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = Comment.objects.filter(article=article)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            return redirect('article_detail', article_id=article_id)
    else:
        form = CommentForm()
    
    return render(request, 'blog/article_detail.html', {'article': article, 'comments': comments, 'form': form})


@login_required(login_url='login')
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('home')
    else:
        form = ArticleForm()
    return render(request, 'blog/create_article.html', {'form': form})

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('create_article')  # Redirigez l'utilisateur vers une page de tableau de bord ou une autre vue après la connexion réussie
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'login/login.html')  # Assurez-vous d'avoir un template HTML nommé "login.html" pour afficher le formulaire de connexion

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('home')

# views.py
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        print('nom valid')
        form = UserRegistrationForm()
    return render(request, 'login/register.html', {'form': form})
