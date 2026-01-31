from django.db import models


class Task(models.Model):
    class Status(models.TextChoices):
        TODO = "todo", "To Do"
        IN_PROGRESS = "in_progress", "In Progress"
        DONE = "done", "Done"

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.TODO)

    def __str__(self) -> str:
        return f"{self.title} ({self.status})"


class TaskRestore(models.Model):
    class Status(models.TextChoices):
        TODO = "todo", "To Do"
        IN_PROGRESS = "in_progress", "In Progress"
        DONE = "done", "Done"

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.TODO)


class About(models.Model):
    name = models.CharField(max_length=50)
    contact = models.IntegerField()
    email = models.EmailField()
    suggestions = models.TextField()
