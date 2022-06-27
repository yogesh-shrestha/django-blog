from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page

app_name = 'blog'
urlpatterns = [
    path('', views.PostView.as_view(), name='index'),
    path('post/<str:slug>', views.PostDetailView.as_view(), name='post'),
    path('add-post/', views.AddPostView.as_view(), name='add-post'),
    path('post/update-post/<int:pk>', views.UpdatePostView.as_view(), name='update-post'),
    path('post/<int:pk>/delete', views.DeletePostView.as_view(), name='delete-post'),
    path('category/<int:cat>', views.CategoryPostView.as_view(), name='cat-posts'),
    path('search/', views.post_search_view, name='post-search'),
    path('sumbit-commit/<str:slug>', views.submit_comment_view, name='submit-commit'),
    path('tag/<int:tag_id>', views.TagPostView.as_view(), name='tag-posts'),
    path('like/<int:pk>', views.like_post_view, name='like-post'),
    path('post-submit', views.PostSubmitView.as_view(), name='post-submit'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)