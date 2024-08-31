# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import User 
from django.contrib.auth.views import LoginView
# Create your views here.
class UserLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('user_list')
    
class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    
class UserDetailView(DetailView):
    model = User
    template_name = 'users/user_detail.html'

class UserCreateView(CreateView):
    model = User 
    fields = ['nombre' , 'email' , 'password' , 'active']
    template_name = 'users/user_create.html'
    success_url = reverse_lazy('user_list')
    
class UserUpdateView(UpdateView):
    model = User
    fields = ['nombre' , 'email' , 'password' , 'active'] 
    template_name = 'users/user_update.html'
    success_url = reverse_lazy('user_list')

class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/userdelete.html'
    success_url = reverse_lazy('user_list')
        