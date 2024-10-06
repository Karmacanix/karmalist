import datetime

now = datetime.datetime.now()

from django.utils import timezone
# Create your models here.
from django.conf import settings
from django.urls import reverse
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


# Create your models here.
class TaskList(models.Model):
    title = models.CharField(max_length=50, blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Task(models.Model):
    PROGRESS_CHOICES = [
        ("TODO", "TO DO"),
        ("INPROGRESS", "IN PROGRESS"),
        ("COMPLETE", "COMPLETE"),
        ("CANCEL", "CANCELLED"),
        ("ONHOLD", "ON HOLD"),
    ]
    title = models.CharField(max_length=50, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    due_date = models.DateField(default=(datetime.date.today() + datetime.timedelta(days=7)))
    task_status = models.CharField(
        choices=PROGRESS_CHOICES,
        default="TODO",
    )
    assigned = models.ForeignKey(User, on_delete=models.CASCADE)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def is_active(self):
        return self.task_status in {self.TODO, self.INPROGRESS}

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})
    
