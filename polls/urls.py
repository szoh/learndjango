from django.urls import path
from . import views

#app_name = 'polls'
urlpatterns = [
    # ex: /something/
    path('', views.index, name='index'),
    # ex: /polls/5/detail/
    path('<int:question_id>/detail/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/choice/', views.choice, name='choice'),
    path('<int:question_id>/choice/', views.choice, name='mzoh'),
    path('<int:question_id>/choice/', views.choice, name='mzoh1'),
    path('', views.index, name='index'),
]