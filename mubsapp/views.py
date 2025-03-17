from django.shortcuts import redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import update_session_auth_hash
from .models import Book, SoftwareCategory, Software
from django.db.models import Q
import os
from googleapiclient.discovery import build
from dotenv import load_dotenv
from django.conf import settings

load_dotenv()  # Load environment variables from .env file

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('landing_page')
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})

@login_required
def landing_page(request):
    return render(request, 'authentication/landing_page.html')

@login_required
def logout_redirect(request):
    logout(request)
    return redirect('login')

@login_required
def custom_logout(request):
    logout(request)
    response = redirect('login')  # Redirect to the login page
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

# Books
@login_required
def books_view(request):
    query = request.GET.get('q', '')
    books_list = Book.objects.filter(
        Q(title__icontains=query) | 
        Q(author__icontains=query) | 
        Q(isbn__icontains=query)
    )
    paginator = Paginator(books_list, 2)  # Show 10 books per page
    page_number = request.GET.get('page')
    books = paginator.get_page(page_number)
    return render(request, 'books.html', {'books': books})

@login_required
def software_view(request):
    category_id = request.GET.get('category', '')
    search_query = request.GET.get('search', '').lower()
    
    software_list = Software.objects.all()
    
    if category_id:
        software_list = software_list.filter(category_id=category_id)
    
    if search_query:
        software_list = software_list.filter(name__icontains=search_query)
    
    paginator = Paginator(software_list, 10)  # Show 10 software items per page
    page_number = request.GET.get('page')
    software_list = paginator.get_page(page_number)
    
    categories = SoftwareCategory.objects.all()
    
    context = {
        'software_list': software_list,
        'categories': categories,
    }
    return render(request, 'software.html', context)

@login_required
def software_detail(request, software_id):
    software = get_object_or_404(Software, id=software_id)
    related_software = software.category.software_set.exclude(id=software_id)
    return render(request, 'software_detail.html', {
        'software': software,
        'related_software': related_software
    })

@login_required
def tutorials(request):
    api_key = os.getenv('YOUTUBE_API_KEY')  # Load API key from environment variable
    youtube = build('youtube', 'v3', developerKey=api_key)

    search_response = youtube.search().list(
        q='programming tutorials',  # Replace with your search query
        part='snippet',
        maxResults=10
    ).execute()

    tutorials = []
    for item in search_response['items']:
        tutorial = {
            'title': item['snippet']['title'],
            'description': item['snippet']['description'],
            'thumbnail': item['snippet']['thumbnails']['default']['url'],
            'videoId': item['id'].get('videoId', '')  # Use get method to avoid KeyError
        }
        tutorials.append(tutorial)

    context = {
        'tutorials': tutorials,
        'youtube_api_key': settings.YOUTUBE_API_KEY
    }
    return render(request, 'tutorials.html', context)



@login_required
def account(request):
    if request.method == 'POST':
        user_form = UserChangeForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile has been updated successfully.')
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in
            messages.success(request, 'Your password has been updated successfully.')
        return redirect('account')
    else:
        user_form = UserChangeForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)
    
    context = {
        'user_form': user_form,
        'password_form': password_form
    }
    return render(request, 'account.html', context)