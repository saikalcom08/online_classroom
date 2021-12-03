from django.http import request, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView

from .forms import UserRegistration, UserEditForm
from django.views import generic
from .models import Course, Topic, Announcement
from .forms import CourseForm, TopicForm, AnnouncementForm
from django.urls import reverse_lazy, reverse
from django.http import Http404

# Create your views here.
def main_page(request):
    return render(request, 'index.html')

@login_required
def dashboard(request):
    announcement = Announcement.objects.filter(created_date__year=2021)
    context = {
        "welcome": "Welcome to your classroom",
        "announcement": announcement
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

#COURSE
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

class CourseDeleteView(generic.DeleteView):
    model = Course
    template_name = 'courses/course_confirm_delete.html'
    success_url = reverse_lazy('online_class:courses')

# TOPIC
class TopicListView(generic.ListView):
    model = Topic
    template_name = 'topics/topics.html'
    context_object_name = 'topic'


class TopicDetailView(generic.DetailView):
    model = Topic
    template_name = 'topics/detail-topics.html'
    context_object_name = 'topics'


class TopicCreateView(generic.CreateView):
    model = Topic
    form_class = TopicForm
    template_name = 'topics/create-topics.html'
    success_url = reverse_lazy('online_class:topics')


class TopicUpdateView(generic.UpdateView):
    model = Topic
    form_class = TopicForm
    template_name = 'topics/update-topics.html'

    def get_success_url(self):
        topic_id = self.kwargs['pk']
        return reverse_lazy('online_class:detail-topics', kwargs={
            'pk': topic_id})

class TopicDeleteView(generic.DeleteView):
    model = Topic
    template_name = 'topics/topic_confirm_delete.html'
    success_url = reverse_lazy('online_class:topics')


#ANNOUNCEMENT
class AnnouncementListView(generic.ListView):
    model = Announcement
    template_name = 'announcement/announcements.html'
    context_object_name = 'announcement'

class AnnouncementCreateView(generic.CreateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = 'announcement/create-announcement.html'
    success_url = reverse_lazy('online_class:announcement')

class AnnouncementUpdateView(generic.UpdateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = 'announcement/update-announcement.html'
    success_url = reverse_lazy('online_class:announcement')

    # def get_success_url(self):
    #     return reverse_lazy('online_class:announcement')



