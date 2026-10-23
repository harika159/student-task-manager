from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import RegisterForm, TaskForm
from .models import Task

def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Welcome! Your account has been created.")
            return redirect("dashboard")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})

@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    status_filter = request.GET.get("status", "")
    if status_filter in ["Pending", "Completed"]:
        tasks = tasks.filter(status=status_filter)
    context = {
        "tasks": tasks,
        "total_count": Task.objects.filter(user=request.user).count(),
        "pending_count": Task.objects.filter(user=request.user, status="Pending").count(),
        "completed_count": Task.objects.filter(user=request.user, status="Completed").count(),
        "current_status": status_filter,
    }
    return render(request, "tasks/dashboard.html", context)

@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, "Task added successfully.")
            return redirect("dashboard")
    else:
        form = TaskForm()
    return render(request, "tasks/task_form.html", {"form": form, "page_title": "Add a task"})

@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully.")
            return redirect("dashboard")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/task_form.html", {"form": form, "page_title": "Edit task"})

@login_required
def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        task.status = "Completed" if task.status == "Pending" else "Pending"
        task.save(update_fields=["status"])
        messages.success(request, "Task status updated.")
    return redirect("dashboard")

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        task.delete()
        messages.success(request, "Task deleted.")
    return redirect("dashboard")
