from django.shortcuts import render, redirect

from .models import Task, TaskRestore, About


def home(request):
    read = Task.objects.all()
    b = {"read": read}
    return render(request, "home.html", b)


def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        status = request.POST.get("status", Task.Status.TODO)
        Task.objects.create(title=title, description=description, status=status)
        return redirect("home")

    return render(request, "create.html", {"status_choices": Task.Status.choices})


def dele(request, id):
    d = Task.objects.get(id=id)
    TaskRestore.objects.create(title=d.title, description=d.description, status=d.status)
    d.delete()
    return redirect("home")


def history(request):
    b = TaskRestore.objects.all()
    d = {"b": b}
    return render(request, "history.html", d)


def upd(request, id):
    s = Task.objects.get(id=id)

    if request.method == "POST":
        s.title = request.POST["title"]
        s.description = request.POST["description"]
        s.status = request.POST.get("status", s.status)
        s.save()
        return redirect("home")

    d = {"k": s, "status_choices": Task.Status.choices}
    return render(request, "create.html", d)


def restore(request, id):
    b = TaskRestore.objects.get(id=id)
    Task.objects.create(title=b.title, description=b.description, status=b.status)
    b.delete()
    return redirect("history")


def dele_restore(request, id):
    b = TaskRestore.objects.get(id=id)
    b.delete()
    return redirect("history")


def restore_all(request):
    b = TaskRestore.objects.all()
    for i in b:
        Task.objects.create(title=i.title, description=i.description, status=i.status)
    b.delete()
    return redirect("history")


def deleteall(request):
    b = TaskRestore.objects.all()
    b.delete()
    return redirect("history")


def about(request):
    return render(request, "about.html")
