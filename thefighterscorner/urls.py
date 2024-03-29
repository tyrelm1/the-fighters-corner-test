from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from django.shortcuts import render
from posts.views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView, add_comment,
    comment_edit, comment_delete
)
from accounts.views import signup_view
from events.views import event_list, event_detail


def custom_page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


urlpatterns = [
    path("about/", include("about.urls"), name="about-urls"),
    path("admin/", admin.site.urls),
    path("summernote/", include("django_summernote.urls")),
    path("", PostListView.as_view(), name="home"),
    path("posts/", include("posts.urls")),
    path("accounts/", signup_view, name="account_signup"),
    path("accounts/", include("allauth.urls")),
    path('events/', include('events.urls')),
]

handler404 = 'thefighterscorner.urls.custom_page_not_found_view'