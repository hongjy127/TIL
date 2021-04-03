from django.urls import path, re_path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', PostLV.as_view(), name='index'),
    # re_path(r'^(?P<slug>[-\w]+)/$', PostDV.as_view(), name='detail'),
    path('<int:pk>/', PostDV.as_view(), name='detail'),

    # /blog/archive/
    path('archive/archive/', PostAV.as_view(), name='post_archive'),
    # /blog/archive/2019/
    path('archive/<int:year>/', PostYAV.as_view(), name='post_year_archive'),
    # /blog/archive/2019/nov/
    path('archive/<int:year>/<str:month>/', PostMAV.as_view(), name='post_month_archive'),
    # /blog/archive/2019/nov/10/
    path('archive/<int:year>/<str:month>/<int:day>/', PostDAV.as_view(), name='post_day_archive'),
    # /blog/archive/today/
    path('archive/today/', PostTAV.as_view(), name='post_today_archive'),
    # Example: /blog/tag/
    path('tag/', TagCloudTV.as_view(), name='tag_cloud'),
    # Example: /blog/tag/tagname/
    path('tag/<str:tag>/', TaggedObjectLV.as_view(), name='tagged_object_list'),
    # Example: /blog/search/
    path('search/', SearchFormView.as_view(), name='search'),

     # Example: /blog/add/
    path('add/', PostCreateView.as_view(), name="add"),
    # Example: /blog/99/update/
    path('<int:pk>/update/', PostUpdateView.as_view(), name="update"),
    # Example: /blog/99/delete/
    path('<int:pk>/delete/', PostDeleteView.as_view(), name="delete"),

    path('download/<int:id>', download, name="download"),
]