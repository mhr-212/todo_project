from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Task
from .forms import TaskForm


class TaskListView(LoginRequiredMixin, ListView):
    """Display list of tasks for the logged-in user."""
    model = Task
    template_name = 'todo/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10

    def get_queryset(self):
        """Return tasks for the current user only."""
        return Task.objects.filter(user=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    """Create a new task."""
    model = Task
    form_class = TaskForm
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('todo:task_list')

    def form_valid(self, form):
        """Set the user before saving."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """Update an existing task."""
    model = Task
    form_class = TaskForm
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('todo:task_list')

    def get_queryset(self):
        """Ensure users can only edit their own tasks."""
        return Task.objects.filter(user=self.request.user)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """Delete a task."""
    model = Task
    template_name = 'todo/task_confirm_delete.html'
    success_url = reverse_lazy('todo:task_list')

    def get_queryset(self):
        """Ensure users can only delete their own tasks."""
        return Task.objects.filter(user=self.request.user)


class TaskToggleView(LoginRequiredMixin, View):
    """Toggle the completed status of a task."""
    
    def post(self, request, pk):
        """Toggle task completion status."""
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.completed = not task.completed
        task.save()
        return HttpResponseRedirect(reverse_lazy('todo:task_list'))


class SignUpView(CreateView):
    """User registration view."""
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('todo:task_list')

    def form_valid(self, form):
        """Log in the user after successful registration."""
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

