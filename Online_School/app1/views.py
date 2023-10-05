from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect,get_object_or_404
from app1.forms import CourseStoreForm
from app1.models import CoursesStoreModel
from category.models import Category
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from django.shortcuts import render,redirect
from .forms import RegisterForm,user_chagne_data
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Upload courses
def ChourseForm(request):
    if request.method == 'POST':
        form = CourseStoreForm(request.POST,request.FILES, prefix = 'form')
        if form.is_valid():
            task_list = form.save(commit=False)
            task_list.teacher_id = request.user
            task_list.save()
            return redirect('home')
    else:
        form = CourseStoreForm(prefix='form')

    return render(request, 'course_store.html',{'form' : form })


# show all course at home page with category also
def show_courses(request, category_slug=None):
    category = None
    course = None
    if category_slug :
        category = get_object_or_404(Category, slug = category_slug)
        course = CoursesStoreModel.objects.filter( dept = category)
        page = request.GET.get('page')
        paginator = Paginator(course, 3)
        paged_course = paginator.get_page(page)
    else:
        course = CoursesStoreModel.objects.all()
        paginator = Paginator(course, 6)
        page = request.GET.get('page')
        paged_course = paginator.get_page(page)

    categories = Category.objects.all()
    return render(request, 'login_home.html',{'data' : paged_course, 'categories': categories})


# Search feature using course title/ course name
def search_feature(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        posts = CoursesStoreModel.objects.filter( course_name = search_query )
        return render(request, 'search_item.html', {'query':search_query, 'post':posts})
    else:
        return render(request, 'search_item.html',{})

# show profile and also show user uploaded course with the feature of delete and edit option
def show_profile(request, profile_slug=None):
    if profile_slug :
        profile1 = get_object_or_404(User, username = profile_slug)
        data = CoursesStoreModel.objects.filter( teacher_id = profile1)
        page = request.GET.get('page')
        paginator = Paginator(data, 2)
        paged_course = paginator.get_page(page)
    else:
        page = request.GET.get('page')
        paginator = Paginator(data, 2)
        paged_course = paginator.get_page(page)
    all_data = CoursesStoreModel.objects.all()
    return render(request, 'profile.html',{'data' : paged_course, 'all_data' : all_data})

# edit course element
class CourseUpdateView(UpdateView):
    model = CoursesStoreModel
    template_name = 'course_store.html'
    form_class = CourseStoreForm
    success_url = reverse_lazy('home')

# delete course
class DeleteCourseView(DeleteView):
    model = CoursesStoreModel
    template_name = 'delete_confirmation.html'
    success_url = reverse_lazy('home')

# Show course Details
class CourseDetailView(DetailView):
    model = CoursesStoreModel
    template_name = 'course_details.html'
    context_object_name = 'i'
    pk_url_kwarg = 'id'

# User signup 
def signup(request):
    if not request.user.is_authenticated:
        if request.method =="POST":
            form = RegisterForm(request.POST) 
            if form.is_valid():
                messages.success(request, 'Account created successfully')
                form.save()
        else:
            form = RegisterForm()
        return render(request, 'signup.html',{'form': form})
    else:
        return redirect('login_home')
    
# user Login
def User_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username = name, password = userpass)   #check kortechi user database e ache ki na
                if user is not None:
                    login(request, user)
                    return redirect('home')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form' : form})
    else:
        return redirect('home')

# home page
def login_home(request):
    if request.user.is_authenticated:
        return render(request, 'login_home.html',{'user' : request.user})
    else:
        return redirect('login')
    
# profile page
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html',{'user' : request.user})
    else:
        return redirect('login')
    
# change login password
def pass_change(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)  # password update korbe
                return redirect('login_home')    
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, './passchange.html', {'form': form})
    else:
        return redirect('signup')
    

# logout
def user_logout(request):
    logout(request)
    return redirect('login')
    
# chagne or edit user info
def ChangeUserData(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            form = user_chagne_data(request.POST, instance = request.user)
            if form.is_valid():
                messages.success(request, 'Account created successfully')
                form.save()
        else:
            form = user_chagne_data(instance = request.user)
        return render(request, 'changeuserdata.html',{'form': form})
    else:
        return redirect('signup')
    
