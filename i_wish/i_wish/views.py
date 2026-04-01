from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm, WishForm
from django.contrib.auth.decorators import login_required
from .models import Wish, CustomUser


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('wish_list')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})


def login_views(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

            return redirect('wish_list')

    else:
        form = CustomUserCreationForm()
        return render(request, 'login.html', {'form': form})


def logout_views(request):
    logout(request)
    return redirect('login')


@login_required
def wish_list(request):
    wishes = Wish.objects.filter(owner=request.user)
    return render(request, 'wish_list.html', {'wishes': wishes})


def public_wishlist(request, user_id):
    owner = CustomUser.objects.filter(id=user_id).first()
    if owner is None:
        return redirect('wish_list')

    wishes = Wish.objects.filter(owner=owner)

    return render(request, "public_wish_list.html", {'owner': owner, 'wishes': wishes})


def add_wish(request):
    if request.method == 'GET':
        form = WishForm()

    elif request.method == "POST":
        form = WishForm(request.POST, request.FILES)
        if form.is_valid():
            wish = form.save(commit=False)
            wish.owner = request.user
            wish.save()
            return redirect('wish_list')


    return render(request, 'add_wish.html', {'form': form})


@login_required
def delete_wish(request, wish_id):
    wish = Wish.objects.filter(id=wish_id, owner=request.user)

    if not wish:
        return redirect('wish_list')

    if request.method == 'POST':

        wish.delete()
        return redirect('wish_list')

    return render(request, 'confirm_delete.html', {'wish': wish})
