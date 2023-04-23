from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, FormView
from .models import Course, Rating
from django.urls import  reverse
from .forms import SearchForm, RatingForm, User
from django.contrib.auth import authenticate, login, logout
def home(request):
    return render(request, 'home.html')


class SearchView(FormView, ListView):
    model = Course
    form_class = SearchForm
    paginate_by = 10
    template_name = "search.html"
    success_url= "/"

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = Course.objects.all()
        query = self.request.GET.get('query')
        courses = self.request.GET.getlist('courses')
        gender = self.request.GET.getlist('gender')
        
        if courses:
            queryset = queryset.filter(course__in=courses)
        if gender:
            queryset = queryset.filter(gender__in=gender)
            
        return queryset
    

def rate_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = user
            rating.save()
            user.rating = user.rating + rating.score
            user.save()
            return redirect('user_profile', user_id=user.id)
    else:
        form = RatingForm()
    return render(request, 'rate_user.html', {'user': user, 'form': form})


def auth_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else: 
                return HttpResponse('Your account is inactive')
        else:
            return HttpResponse("somebody tried to login and failed")
        
    return render(request, 'login.html',{})
        
