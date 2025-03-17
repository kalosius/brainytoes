from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Book
from django.db.models import Q


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
    paginator = Paginator(books_list, 5)  # Show 10 books per page
    page_number = request.GET.get('page')
    books = paginator.get_page(page_number)
    
    return render(request, 'books.html', {'books': books})

@login_required
def software(request):
    return render(request, 'software.html')

@login_required
def tutorials(request):
    return render(request, 'tutorials.html')

@login_required
def account(request):
    return render(request, 'account.html')