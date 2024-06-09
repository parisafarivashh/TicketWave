from django.urls import path

from authorize.views import TokenController, RegisterView, ChangePasswordView

urlpatterns = [
    path('login', TokenController.as_view(), name='login'),
    path('sign-up', RegisterView.as_view(), name='sign-up'),
    path('set-password', ChangePasswordView.as_view(), name='set-password'),
]

