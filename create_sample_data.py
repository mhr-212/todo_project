#!/usr/bin/env python
"""
Script to create sample data for the Django To-Do application.
"""
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append('/home/ubuntu/todo_project')

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_project.settings')
django.setup()

from django.contrib.auth.models import User
from todo.models import Task

def create_sample_data():
    """Create sample tasks for testing."""
    
    # Get or create the admin user
    admin_user, created = User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@example.com',
            'is_staff': True,
            'is_superuser': True,
        }
    )
    
    if created:
        admin_user.set_password('admin123')
        admin_user.save()
        print(f"Created admin user: {admin_user.username}")
    else:
        print(f"Admin user already exists: {admin_user.username}")
    
    # Create sample tasks
    sample_tasks = [
        {
            'title': 'Complete Django project documentation',
            'description': 'Write comprehensive documentation for the Django To-Do application including setup instructions, features, and usage examples.',
            'completed': False,
        },
        {
            'title': 'Review code and fix bugs',
            'description': 'Go through the codebase to identify and fix any potential bugs or improvements.',
            'completed': True,
        },
        {
            'title': 'Design user interface improvements',
            'description': 'Create mockups for enhanced user interface with better user experience.',
            'completed': False,
        },
        {
            'title': 'Set up automated testing',
            'description': 'Implement unit tests and integration tests for all major functionality.',
            'completed': False,
        },
        {
            'title': 'Deploy to production server',
            'description': 'Configure production environment and deploy the application.',
            'completed': False,
        },
    ]
    
    # Create tasks for admin user
    created_count = 0
    for task_data in sample_tasks:
        task, created = Task.objects.get_or_create(
            title=task_data['title'],
            user=admin_user,
            defaults={
                'description': task_data['description'],
                'completed': task_data['completed'],
            }
        )
        if created:
            created_count += 1
            print(f"Created task: {task.title}")
        else:
            print(f"Task already exists: {task.title}")
    
    print(f"\nSample data creation complete!")
    print(f"Created {created_count} new tasks")
    print(f"Total tasks for {admin_user.username}: {Task.objects.filter(user=admin_user).count()}")

if __name__ == '__main__':
    create_sample_data()

