from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
app_name = 'myapp'
urlpatterns = [
    
    path('',views.index, name='index'),
    path('success/',views.success,name='success'),

     # urls for password reset
    #1. for entering email to reset password
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='pwdresetapp/password_reset.html',
    
    success_url=reverse_lazy('myapp:password_reset_done')),
         name='password_reset'),

    #2. for sending email to user who want to change password
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='pwdresetapp/password_reset_sent.html'),
         name='password_reset_done'),
    
    # # 3. The link from email on which user clicks to reset password
    # path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='pwdresetapp/password_reset_fill.html'),
    #      name='password_reset_confirm'),
    # # 4. on successful reset of password
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='pwdresetapp/password_reset_complete.html'),
    #      name='password_reset_complete'),
    

]