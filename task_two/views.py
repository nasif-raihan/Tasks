from django.shortcuts import render, redirect
from .models import User
from task_two.forms import UserForm


def home(request):
    return render(request, "base.html", context={"title": home})


def add_data(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user_data = User.objects.all()
            return render(
                request,
                "task_two/retrieve.html",
                context={"title": "User Data", "users": user_data},
            )
    return render(
        request, "task_two/add.html", context={"title": "Add User", "form": form}
    )


def retrieve_data(request):
    user_data = User.objects.all()
    return render(
        request,
        "task_two/retrieve.html",
        context={"title": "User Data", "users": user_data},
    )


def update_data(request, uid: int):
    current_data = User.objects.get(uid=uid)
    form = UserForm(instance=current_data)

    if request.method == "POST":
        form = UserForm(request.POST, instance=current_data)
        if form.is_valid():
            form.save()
            user_data = User.objects.all()
            return render(
                request,
                "task_two/retrieve.html",
                context={"title": "User Data", "users": user_data},
            )
    return render(
        request, "task_two/update.html", context={"title": "Update User", "form": form}
    )


def delete_data(request, uid):
    try:
        user = User.objects.get(uid=uid)
        print(user)
        user.delete()
        user_data = User.objects.all()
        return render(
            request,
            "task_two/retrieve.html",
            context={"title": "User Data", "users": user_data},
        )
    except User.DoesNotExist:
        return redirect("/task_two")
