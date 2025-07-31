from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Task(models.Model):
    """
    Task model representing a to-do item.
    
    Each task is associated with a user and contains:
    - title: Short description of the task
    - description: Detailed description (optional)
    - completed: Boolean indicating if task is done
    - created_at: Timestamp when task was created
    - updated_at: Timestamp when task was last modified
    """
    title = models.CharField(
        max_length=200,
        help_text="Brief title for the task"
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Detailed description of the task (optional)"
    )
    completed = models.BooleanField(
        default=False,
        help_text="Whether the task has been completed"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks',
        help_text="User who owns this task"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="When the task was created"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="When the task was last updated"
    )

    class Meta:
        ordering = ['-created_at']  # Show newest tasks first
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        """String representation of the task."""
        status = "✓" if self.completed else "○"
        return f"{status} {self.title}"

    def get_absolute_url(self):
        """Return the URL to view this task."""
        return reverse('todo:task_list')

