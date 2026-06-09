from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserCreateForm
from .models import User
from groups.models import Group


def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)

        if form.is_valid():
            user = form.save()
            group = form.cleaned_data.get('group')

            if group and user.role == 'student':
                group.participants.add(user)

            return redirect('/groups/')
    else:
        form = UserCreateForm()

    return render(request, 'users/create.html', {'form': form})


def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('/groups/')