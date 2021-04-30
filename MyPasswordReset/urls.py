"""MyPasswordReset URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pwdresetapp.urls')),

    # 3. The link from email on which user clicks to reset password
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='pwdresetapp/password_reset_fill.html'),
         name='password_reset_confirm'),
    # 4. on successful reset of password
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='pwdresetapp/password_reset_complete.html'),
         name='password_reset_complete'),
   
]
