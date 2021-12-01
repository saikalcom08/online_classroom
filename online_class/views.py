from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration, UserEditForm
from django.views import generic
from .models import Course
from .forms import CourseForm
from django.urls import reverse_lazy, reverse
from django.http import Http404

# Create your views here.
def main_page(request):
    return render(request, 'index.html')

@login_required
def dashboard(request):
    context = {
        "welcome": "Welcome to your classroom"
    }
    return render(request, 'authapp/dashboard.html', context=context)


def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data.get('password')
            )
            new_user.save()
            return render(request, 'authapp/register_done.html')
    else:
        form = UserRegistration()

    context = {
        "form": form
    }

    return render(request, 'authapp/register.html', context=context)


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
    context = {
        'form': user_form,
    }
    return render(request, 'authapp/edit.html', context=context)


class CourseListView(generic.ListView):
    model = Course
    template_name = 'courses/courses.html'
    context_object_name = 'course'


class CourseDetailView(generic.DetailView):
    model = Course
    template_name = 'courses/detail-courses.html'
    context_object_name = 'course'


class CourseCreateView(generic.CreateView):
    form_class = CourseForm
    template_name = 'courses/create-courses.html'
    success_url = reverse_lazy('online_class:courses')

class CourseUpdateView(generic.UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/update-courses.html'

    def get_success_url(self):
        course_id = self.kwargs['pk']
        return reverse_lazy('online_class:detail-courses', kwargs={
            'pk': course_id})

# class CourseDeleteView(generic.DeleteView):
#     def get_object(self, queryset=None):
#         """ Hook to ensure object is owned by request.user. """
#         obj = super(CourseDeleteView, self).get_object()
#         if not obj.owner == self.request.user:
#             raise Http404
#         return obj


class CourseDeleteView(generic.DeleteView):
    model = Course
    template_name = 'courses/course_confirm_delete.html'
    success_url = reverse_lazy('online_class:courses')

    # def get_success_url(self):
    #     return reverse('dashboard')
