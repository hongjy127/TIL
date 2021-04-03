from django.urls import path
from django.urls.resolvers import URLPattern
from polls import views
    
app_name = 'polls'  # polls 앱의 namespace명

urlpatterns = [
    # /polls/
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]