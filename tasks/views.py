from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from tasks.models import Task, TaskList
# Create your views here.


class TaskListView(ListView):
    model = TaskList
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_task_list"] = TaskList.objects.filter(owner=self.request.user)
        return context
    # def get_queryset(self):
    #     user = self.request.user
    #     users_task_list = TaskList.objects.filter(owner=user)
    #     return users_task_list


class TaskView(ListView):
    model = Task
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # need task list from request something like request.kwargs.get['task_list id] 
        context["parentlist"] = TaskList.objects.get(id=self.kwargs['tasklist_id'])
        context["list_tasks"] = Task.objects.filter(task_list=self.kwargs['tasklist_id'])
        #context["user_task_list"] = TaskList.objects.filter(owner=self.request.user)
        return context
    # def get_queryset(self):
    #     user = self.request.user
    #     users_task_list = TaskList.objects.filter(owner=user)
    #     return users_task_list