from django.urls import path
from .views import (
    PostListView,
    PostUpdateView,
    PostDetailView,
    PostDeleteView,
    PostCreateView,
    PostCommentView,

    )
urlpatterns = [
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/comment/', PostCommentView.as_view(), name='add_comment'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('new/', PostCreateView.as_view(), name='post_new'),
    path('', PostListView.as_view(), name='post_list')
    ]
