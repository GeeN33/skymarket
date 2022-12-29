from django.urls import path
from ads import views

urlpatterns = [

    path('ad/', views.AdListView.as_view()),
    path('ad/<int:pk>/update/', views.AdUpdateView.as_view()),
    path('ad/<int:pk>/delete/', views.AdDeleteView.as_view()),
    path('ad/<int:pk>/', views.AdDetailView.as_view()),
    path('ad/create/', views.AdCreateView.as_view()),


    path('comment/create/', views.CommentCreateView.as_view()),
    path('comment/', views.CommentListView.as_view()),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view()),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view()),

]