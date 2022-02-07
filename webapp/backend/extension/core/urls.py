from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework import routers
from .views import *


urlpatterns = [
    path('api/v1/notes/', NoteUserList.as_view()),
    path('api/v1/notes/<int:pk>/', NoteDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('api-auth/registration/', CreateUserView.as_view()),
    path('api/v1/token/', TokenObtainPairView.as_view()),
    path('api/v1/token/refresh/', TokenRefreshView.as_view())
]
