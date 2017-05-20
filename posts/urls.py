from django.conf.urls import url

from views import PostDetailView, PostListView

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post-list'),
    url(r'^(?P<pk>[0-9]+)/$', PostDetailView.as_view(), name='post-detail'),
]
