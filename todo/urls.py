from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views  


app_name = 'todo' 
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('home', views.home, name='home'),
    path('log_in/', views.log_in, name='log_in'),
    path('addtask/', views.addtask, name='addtask'),
    path('task/<int:task_id>/', views.task, name='task'),
    path('updatetask/<int:task_id>/', views.updatetask, name='updatetask'),
    path('complete/<int:task_id>/', views.complete, name='complete'),
    path('delete/<int:task_id>/', views.deletetask, name='delete'),
    path('log_out', views.log_out, name='logout'),
    
    # resetting the password
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='todo/registration/password_reset_form.html', 
        email_template_name='todo/registration/password_reset_email.html',
        success_url=reverse_lazy('todo:password_reset_done')), # we use reverse lazy to help us call the url only when it's called.
        name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='todo/registration/password_reset_done.html'), 
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='todo/registration/password_reset_confirm.html', 
        success_url=reverse_lazy('todo:password_reset_complete')), 
        name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(
        template_name='todo/registration/password_reset_complete.html'), 
        name='password_reset_complete'),

        # the documentation once said that the when replying the person asking for password by sending him the token, it's not all that safe. and 
        # to make it more safe, you have to use a third party application. look into that when you get time.a
]