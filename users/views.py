from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse

from .models import User
from .forms import UserForm, EditUserForm

def index(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'users/index.html', context)

def new_user(request):
    form = UserForm()
    context = {'form': form}
    return render(request, 'users/new_user.html', context)

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponse('Form succes!')
        else:
            message = "Something wrong with what you entered!"
            context = {'form': form, 'message': message}
            return render(request, 'users/new_user.html', context)
    else:
        form = UserForm()

    return HttpResponse("hi am being debugged!")

def edit(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponse('Edit success!')
        else:
            form = EditUserForm(request.POST, instance=user)
            return render(request, 'users/edit.html', {'form': form})
    else:
        form = EditUserForm(instance=user)
        message = 'Editing user'
        context = {'user': user, 'form': form, 'message': message}
        return  render(request, 'users/edit.html', context)