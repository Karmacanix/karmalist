from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from tasks.models import Task, TaskList
# Create your views here.


class TaskList(ListView):
    model = TaskList
    fields = ['title', 'owner']
	# def get_queryset(self):
	# 	user = self.request.user
	# 	users_project_list = ProjectTeam.objects.filter(user=user).values_list('project', flat=True)
	# 	return Project.objects.filter(id__in=users_project_list)