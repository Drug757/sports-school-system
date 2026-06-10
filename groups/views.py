from django.shortcuts import render, redirect, get_object_or_404
from .models import Group
from .forms import GroupForm
from users.models import User


def group_list(request):
    groups = Group.objects.all()
    return render(request, "groups/list.html", {"groups": groups})


def create_group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/groups/")
    else:
        form = GroupForm()

    return render(request, "groups/create.html", {"form": form})


def group_detail(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    users = User.objects.all()

    return render(request, "groups/detail.html", {"group": group, "users": users})


def add_user_to_group(request, group_id, user_id):
    group = get_object_or_404(Group, id=group_id)
    user = get_object_or_404(User, id=user_id)

    group.participants.add(user)
    return redirect(f"/groups/{group_id}/")


def remove_user_from_group(request, group_id, user_id):
    group = get_object_or_404(Group, id=group_id)
    user = get_object_or_404(User, id=user_id)

    group.participants.remove(user)
    return redirect(f"/groups/{group_id}/")
