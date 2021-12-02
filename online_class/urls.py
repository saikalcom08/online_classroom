from django.urls import path
from .views import edit, dashboard, register, CourseListView, CourseCreateView, CourseDetailView, CourseUpdateView, \
    CourseDeleteView, TopicListView, TopicDetailView, TopicCreateView, TopicUpdateView, TopicDeleteView, \
    AnnouncementListView, AnnouncementCreateView
from django.urls import reverse_lazy
from .views import main_page
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetDoneView, PasswordResetView,
                                       PasswordResetCompleteView, PasswordResetConfirmView,
                                       PasswordChangeView, PasswordChangeDoneView,
                                       PasswordResetDoneView)

app_name = 'online_class'

urlpatterns = [
    path('', main_page, name='main_page'),
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='authapp/logged_out.html'), name='logout'),
    path('password_change/', PasswordChangeView.as_view(
        template_name='authapp/password_change_form.html'), name='password_change'),
    path('password_change/dond/', PasswordChangeDoneView.as_view(template_name='authapp/password_change_done.html'),
         name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(
        template_name='authapp/password_reset_form.html',
        email_template_name='authapp/password_reset_email.html',
        success_url=reverse_lazy('authapp:password_reset_done')), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='authapp/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='authapp/password_reset_confirm.html',
        success_url=reverse_lazy('online_course:login')), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='authapp/password_reset_complete.html'), name='password_reset_complete'),
    path('courses/', CourseListView.as_view(template_name='courses/courses.html'), name='courses'),
    path('courses/create-courses/', CourseCreateView.as_view(template_name='courses/create-courses.html'), name='create-courses'),
    path('courses/detail-courses/<int:pk>/', CourseDetailView.as_view(), name='detail-courses'),
    path('courses/update-courses/<int:pk>/', CourseUpdateView.as_view(template_name='courses/update-courses.html'), name='update-courses'),
    path('courses/delete-courses/<int:pk>/', CourseDeleteView.as_view(), name='delete-courses'),
    path('topics/', TopicListView.as_view(template_name='topics/topics.html'), name='topics'),
    path('topics/create-topics/', TopicCreateView.as_view(template_name='topics/create-topics.html'), name='create-topics'),
    path('topics/detail-topics/<int:pk>/', TopicDetailView.as_view(), name='detail-topics'),
    path('topics/update-topics/<int:pk>/', TopicUpdateView.as_view(template_name='topics/update-topics.html'), name='update-topics'),
    path('topics/delete-topics/<int:pk>/', TopicDeleteView.as_view(), name='delete-topics'),
    path('announcement/', AnnouncementListView.as_view(template_name='announcement/announcements.html'), name='announcement'),
    path('announcement/create-announcement/', AnnouncementCreateView.as_view(template_name='announcement/create-announcement.html'), name='create-announcement'),
]